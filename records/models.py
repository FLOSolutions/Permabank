from django.core.exceptions import ObjectDoesNotExist
from django.db import models


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
                             related_name='records_created')
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
    sender = models.ForeignKey('profiles.Profile',
            related_name='sent_responses')
    recipient = models.ForeignKey('profiles.Profile',
            related_name='received_responses')
    parent = models.ForeignKey('self', null=True)
    text = models.TextField()
