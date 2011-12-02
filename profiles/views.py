from django.views.generic import DetailView, TemplateView, UpdateView, ListView

from django.contrib.auth.models import User

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
    template_name = 'profile.html'
    max_records = 10  # max. records to display in activity stream

    def get_context_data(self, **kwargs):
        """ Adds records recently created by user to the context """
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        records = self.object.records_created.order_by(
                '-created')[:self.max_records]
        context['records'] = [record.child for record in records]
        return context

@requires_login
class ProfileUpdateView(ProfileViewMixin, UpdateView):
    pass

@requires_login
class UserUpdateView(UpdateView):
    context_object_name = "profile"
    template_name = "profiles/edit.html"

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
