from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ Represents a user's profile """
    user = models.OneToOneField(User, primary_key=True)

class UserForm(forms.ModelForm):
    class Meta:
        model = User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ On user creation, automatically create associated user """
    if created:
        Profile.objects.create(user=instance)
