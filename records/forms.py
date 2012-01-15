from django import forms
from django.template.defaultfilters import filesizeformat
from django.conf import settings

from messaging.forms import ComposeForm

from records.models import Wish, Gift

class UserCreatedModelForm(forms.ModelForm):
    """
    A form for objects that save a reference to their creator. Takes optional
    'user' kwarg, and assigns it to obj.user before saving.
    """

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserCreatedModelForm, self).__init__(*args, **kwargs)

    def clean_picture(self):
        picture = self.cleaned_data['picture']
        
        if picture._size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                'Images cannot be larger than %s. (Uploaded image size was %s.)' % 
                (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(picture._size))
            )

        return picture

    def save(self, commit=True):
        """ Auto-set user """
        obj = super(UserCreatedModelForm, self).save(commit=False)
        if obj.user is None:
            obj.user = self.user
        if commit:
            obj.save()
        return obj

class WishForm(UserCreatedModelForm):
    class Meta:
        fields = ['title', 'description', 'location', 'category', 'picture']
        model = Wish

class GiftForm(UserCreatedModelForm):
    class Meta:
        fields = ['title', 'description', 'location', 'category', 'picture']
        model = Gift
