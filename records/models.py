from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from messaging.models import Message
from profiles.models import Profile

# Managers


class FeaturedManager(models.Manager):
    """
    Custom manager for record model types. Fetches active, featured records,
    ordered by creation date (descending).
    """
    def get_query_set(self):
        queryset = super(FeaturedManager, self).get_query_set()
        return queryset.select_related('wish', 'gift').filter(
                is_featured=True, status=0).order_by('-created')


class WithChildrenManager(models.Manager):
    """ Custom manager for Record that left joins wishes and records """

    use_for_related_fields = True

    def get_query_set(self):
        queryset = super(WithChildrenManager, self).get_query_set()
        return queryset.select_related('wish', 'gift')


# Models


class Category(models.Model):
    """ Entry categories: things like 'space', 'skill', etc. """
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    # todo(ori): are we still doing icons for categories?
    # icon = models.ImageField()

    class Meta:
        verbose_name_plural = 'categories'
    
    def __unicode__(self):
        return self.name
    

class Record(models.Model):
    """ Base class for Gifts and Wishes """
    status_choices = {
        0: 'Active',
        1: 'Abandoned',
        2: 'Completed',
    }

    # the parties involved
    user = models.ForeignKey('profiles.Profile', db_index=True,
                             related_name='records_created', editable=False)
    other_user = models.ForeignKey('profiles.Profile', blank=True, null=True,
                                   related_name='records_fulfilled')

    # timestamps
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Last updated")

    # metadata
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True,
            default='/static/placeholder.jpg')
    title = models.CharField(max_length=140)
    description = models.TextField()
    location = models.CharField(max_length=256)
    contact_info = models.CharField(max_length=256)
    category = models.ForeignKey(Category, db_index=True)
    is_featured = models.BooleanField()
    status = models.PositiveSmallIntegerField(
            choices=status_choices.items(), db_index=True, default=0)

    # managers
    objects = WithChildrenManager()
    featured = FeaturedManager()

    @property
    def type(self):
        return type(self.child).__name__

    @property
    def child(self):
        """ Cast a Record into its corresponding Wish or Gift object """
        try:
            # If the record is a Gift, self.wish will evaluate to None (if we
            # pulled it in via `select_related`) or raise an exception (if we
            # hadn't.)
            assert self.wish is not None
        except (ObjectDoesNotExist, AssertionError):
            return self.gift
        else:
            return self.wish

    @property
    def status_name(self):
        return Record.status_choices[self.status]

    @property
    def short_title(self):
        return self.title[:17] + '...' if len(self.title) > 20 else self.title

    def mark_completed(self):
        if self.status == 0: # active
            self.status = 2  # completed

    def get_absolute_url(self):
        return self.child.get_absolute_url()

    def __unicode__(self):
        return "{user}: {title}".format(user=self.user, title=self.short_title)


class Wish(Record):
    """ Model for user wishes """
    record = models.OneToOneField(Record, parent_link=True)
    subject_prefix = 'wish for'

    # Managers
    objects = models.Manager()
    featured = FeaturedManager()

    class Meta:
        verbose_name_plural = 'wishes'

    @models.permalink
    def get_absolute_url(self):
        return ('wish', (), {'pk': self.id})


class Gift(Record):
    """ Model for user gifts """
    record = models.OneToOneField(Record, parent_link=True)
    subject_prefix = 'gift of'

    # Managers
    objects = models.Manager()
    featured = FeaturedManager()

    @models.permalink
    def get_absolute_url(self):
        return ('gift', (), {'pk': self.id})


class RecordResponse(models.Model):
    """ Represent an interaction between users regarding a record """

    record = models.ForeignKey(Record)

    # sender
    user = models.ForeignKey('profiles.Profile', db_index=True,
                             related_name='sent_responses', editable=False)
    # recipient
    other_user = models.ForeignKey('profiles.Profile',
                                   related_name='received_responses')

    message = models.OneToOneField(Message, blank=True)

    @staticmethod
    def _validate(giver, wisher, record):
        if giver == wisher:
            raise Exception("Giver and wisher must be different")
        if (record.type == 'Wish' and record.user != wisher) or (record.type == 'Gift' and record.user != giver):
            raise Exception("Invalid data")
        if record.status != 0:
            raise Exception("Record is not active")


class YoureWelcome(RecordResponse):
    """ Assertion or acknowledgement that I gave a gift/fulfilled a wish """

    response = models.OneToOneField(RecordResponse, parent_link=True)
    thank_you = models.ForeignKey('records.ThankYou', null=True, blank=True)

    objects = models.Manager()

    @models.permalink
    def get_absolute_url(self):
        return ('welcome', (), {'pk': self.id})

    @property    
    def has_reply(self):
        try:
            return self.thank_you is not None
        except ObjectDoesNotExist:
            return False

    def _generate_request_message(self, giver, wisher, record):
        return Message(
                subject = 'Will you write me a thank-you note for %s?' % record.short_title,            
                body = 'Please write a public note to let people know what you thought about the %s.' % record.title,
                sender = giver.user,
                recipient = wisher.user,
                record = record
        )

    def _generate_accept_message(self, giver, wisher, record):
        return Message(
                subject = "Thanks for the note!",            
                body = "You're welcome for the %s." % record.title,
                sender = giver.user,
                recipient = wisher.user,
                record = record
        )

    def _find_corresponding_thank_you(self, giver, wisher, record):
        thankyous = ThankYou.objects.filter(record=record,user=wisher,other_user=giver).order_by('-pk')
        if len(thankyous) > 0:
            return thankyous[0]
        else:
            return None

    def create(self, commit=True):
        giver = Profile.objects.get(pk=self.user_id)
        wisher = Profile.objects.get(pk=self.other_user_id)
        record = Record.objects.get(pk=self.record_id)

        RecordResponse._validate(giver, wisher, record)

        thank_you = self._find_corresponding_thank_you(giver, wisher, record)
        if thank_you:
            self.thank_you = thank_you
            message = self._generate_accept_message(giver, wisher, record) 
            record.mark_completed()
        else:
            message = self._generate_request_message(giver, wisher, record)
 
        if commit:
            message.save()
            
            self.message = message
            self.save()

            if thank_you:
               record.save()

class ThankYou(RecordResponse):
    """ Assertion or acknowledgement that I recieved a gift/had my wish fulfilled """

    response = models.OneToOneField(RecordResponse, parent_link=True)
    youre_welcome = models.ForeignKey('records.YoureWelcome', null=True, blank=True)
    note = models.TextField()    

    objects = models.Manager()

    @models.permalink
    def get_absolute_url(self):
        return ('thanks', (), {'pk': self.id})

    @property    
    def has_reply(self):
        try:
            return self.youre_welcome is not None
        except ObjectDoesNotExist:
            return False

    def _generate_message(self, giver, wisher, record):
        return Message(
                subject = 'Thanks for the %s!' % record.short_title,            
                body = self.note,
                sender = wisher.user,
                recipient = giver.user,
                record = record
        )

    def _find_corresponding_youre_welcome(self, giver, wisher, record):
        welcomes = YoureWelcome.objects.filter(record=record,user=giver,other_user=wisher).order_by('-pk')
        if len(welcomes) > 0:
            return welcomes[0]
        else:
            return None

    def create(self, commit=True):
        giver = Profile.objects.get(pk=self.other_user_id)
        wisher = Profile.objects.get(pk=self.user_id)
        record = Record.objects.get(pk=self.record_id)

        RecordResponse._validate(giver, wisher, record)

        message = self._generate_message(giver, wisher, record)

        welcome = self._find_corresponding_youre_welcome(giver, wisher, record)
        if welcome:
            self.youre_welcome = welcome
            record.mark_completed()

        if commit:
            message.save()
            
            self.message = message            
            self.save()

            if welcome:
                record.save()
