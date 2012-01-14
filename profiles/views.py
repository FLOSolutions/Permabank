from django.views.generic import DetailView, TemplateView, UpdateView, ListView
from django.http import Http404
from django.contrib.auth.models import User
from django.forms import ModelForm

from profiles.models import Profile
from records.models import Gift, Wish
from utils import requires_login

class TestView(TemplateView):
    template_name = "test.html"

class ProfileViewMixin(object):
    context_object_name = "profile"
    model = Profile

class ProfileListView(ProfileViewMixin, ListView):
    pass

class ProfileDetailView(ProfileViewMixin, DetailView):
    max_records = 10  # max. records to display in activity stream

    def get_context_data(self, **kwargs):
        """ Adds records recently created by user to the context """ 
        records =  self.object.records_created.order_by('-created')
        
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['active_records'] = records.filter(status=0)[:self.max_records]
        context['fulfilled_records'] = records.filter(status=2)[:self.max_records]
        return context

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','tags',)

@requires_login
class ProfileUpdateView(UpdateView):
    context_object_name = "profile"
    form_class = ProfileUpdateForm
    template_name = "profiles/edit.html"
    
    def get_object(self):
        return Profile.objects.get(user__pk=self.request.user.pk)

class ProfileRecordsView(TemplateView):
    template_name = "profiles/records.html"

    def get_context_data(self, **kwargs):
        profile_id = self.kwargs.get('profile_id')
        try:
            profile = Profile.objects.get(pk=profile_id)
        except Profile.DoesNotExist:
            raise Http404
        return {
            'profile': profile,
            'gifts': Gift.objects.filter(user__pk=profile_id).order_by('-created'),
            'wishes': Wish.objects.filter(user__pk=profile_id).order_by('-created'),
        }
