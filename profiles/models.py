from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from taggit.managers import TaggableManager


class ProfileManager(models.Manager):
    """ Custom Manager for Profile model """

    use_for_related_fields = True

    def get_query_set(self):
        # optimization: auto select-related the related User object
        query_set = super(ProfileManager, self).get_query_set()
        return query_set.select_related('user')


class Profile(models.Model):
    """ Represents a user's profile """

    user = models.OneToOneField(User, primary_key=True)
    location = models.CharField(max_length=64, null=True, blank=True)
    hometown = models.CharField(max_length=64, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    praises = models.TextField(null=True, blank=True)
    grievances = models.TextField(null=True, blank=True)

    ############################
    # social media integration #
    ############################
    facebook_username = models.CharField(max_length=50, blank=True, null=True)
    twitter_username = models.CharField(max_length=15, blank=True, null=True)
    tumblr_name = models.CharField(max_length=64, blank=True, null=True)
    vimeo_username = models.CharField(max_length=64, blank=True, null=True)

    ############
    # managers #
    ############
    objects = ProfileManager()
    tags = TaggableManager()

    @models.permalink
    def get_absolute_url(self):
        return ('profile', (), {'pk': self.pk})

    def __unicode__(self):
        """ Unicode representation of user profiles """
        full_name = self.user.get_full_name()
        if not full_name:
            return self.user.username
        else:
            return u"%s (%s)" % (self.user.username, full_name)


class UserForm(forms.ModelForm):

    class Meta:
        model = User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ On user creation, automatically create associated user """
    if created:
        profile = Profile.objects.get_or_create(user=instance)
