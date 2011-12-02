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
    template_name = "profiles/profile.html"
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        #context['gifts'] = Gift.objects.order_by('-created', 'title').filter(user__pk=self.object.pk)[:5]
        #context['wishes'] = Wish.objects.order_by('-created', 'title').filter(user__pk=self.object.pk)[:5]
        list1 = list(Gift.objects.order_by('-created', 'title').filter(user__pk=self.object.pk)[:5])
        list2 = list(Wish.objects.order_by('-created', 'title').filter(user__pk=self.object.pk)[:5])
        list3 = list1 + list2
        context['giftswishes'] = sorted(list3, key=lambda record: record.pk, reverse=True)
        
            
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
