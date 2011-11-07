from django import forms
from permabank.records.models import Wish, Request

class WishForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'description', 'location', 'category', 'picture']
        model = Wish
