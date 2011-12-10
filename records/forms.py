from django import forms
from permabank.messaging.forms import ComposeForm

from records.models import Wish, Gift

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
