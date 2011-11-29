from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    location = models.CharField(max_length=64)
    bio = models.TextField()
    objects = ProfileManager()

    def __unicode__(self):
        """ Unicode representation of user profiles """
        full_name = self.user.get_full_name()
        email = self.user.email
        if not full_name:
            return email
        else:
            return u"%s (%s)" % (email, full_name)

class UserForm(forms.ModelForm):
    class Meta:
        model = User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ On user creation, automatically create associated user """
    if created:
        Profile.objects.create(user=instance)
