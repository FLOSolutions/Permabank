from django.core.exceptions import ObjectDoesNotExist
from django.db import models

def _truncate_title(title):
    return title[:17] + '...' if len(title) > 20 else title

class FeaturedManager(models.Manager):
    """
    Custom manager for record model types. Fetches active, featured records,
    ordered by creation date (descending).
    """
    def get_query_set(self):
        queryset = super(FeaturedManager, self).get_query_set()
        return queryset.filter(is_featured=True, status=0).order_by('-created')

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
    status = models.PositiveSmallIntegerField(choices=status_choices.items(),
                                              db_index=True, default=0)

    # managers
    featured = FeaturedManager()

    def get_child(self):
        """ Gets the current Record object as an instance of its subclass """
        # todo(ori): this is a hack to allow list_filter by subtype in the
        # admin, but maybe it's not necessary. take out if unused.
        for child_model in (Wish, Request):
            if child_model.objects.filter(pk=self.pk).exists():
                return child_model
        raise ObjectDoesNotExist("Record has no child.")

    def __unicode__(self):
        # truncate to 20 characters
        title = self.title
        if len(title) > 20:
            title = title[:17] + '...'
        return "{user}: {title}".format(user=self.user, title=title)

class Wish(Record):
    """ Model for user wishes """
    record = models.OneToOneField(Record, parent_link=True)

    class Meta:
        verbose_name_plural = 'wishes'


class Gift(Record):
    """ Model for user gifts """
    record = models.OneToOneField(Record, parent_link=True)
