from django import forms
from django.template.defaultfilters import filesizeformat
from django.conf import settings
from django.core.files import File

from messaging.forms import ComposeForm
from messaging.models import Message

from records.models import Record, Wish, Gift, ThankYou, YoureWelcome

from profiles.models import Profile

class UserCreatedModelForm(forms.ModelForm):
    """
    A form for objects that save a reference to their creator. Takes optional
    'user' kwarg, and assigns it to obj.user before saving.
    """

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserCreatedModelForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """ Auto-set user """
        obj = super(UserCreatedModelForm, self).save(commit=False)

        has_user = False
        try:
            has_user = obj.user is not None
        except:
            pass

        if not has_user:
            obj.user = self.user
        if commit:
            obj.save()
        return obj

class ThankYouForm(UserCreatedModelForm):
    class Meta:
        fields = ['record', 'other_user', 'note']
        model = ThankYou

#    TODO Make record, and (if present) other user, readonly

    def save(self, commit=True):
        """ Create message """
        obj = super(ThankYouForm, self).save(commit=False)
        obj.create(commit=commit)
        return obj

class YoureWelcomeForm(UserCreatedModelForm):
    class Meta:
        fields = ['record', 'other_user']
        model = YoureWelcome

#    TODO Make record, and (if present) other user, readonly

    def save(self, commit=True):
        """ Create message """
        obj = super(YoureWelcomeForm, self).save(commit=False)
        obj.create(commit=commit)
        return obj

class RecordForm(UserCreatedModelForm):
    def clean_picture(self):
        picture = self.cleaned_data['picture']
               
        if picture is not None and isinstance(picture, File) and picture._size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                'Images cannot be larger than %s. (Uploaded image size was %s.)' % 
                (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(picture._size))
            )

        return picture

class WishForm(RecordForm):
    class Meta:
        fields = ['title', 'description', 'location', 'category', 'picture']
        model = Wish

class GiftForm(RecordForm):
    class Meta:
        fields = ['title', 'description', 'location', 'category', 'picture']
        model = Gift

