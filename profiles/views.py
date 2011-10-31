from django.views.generic import DetailView
from profiles.models import Profile

class ProfileViewMixin(object):
    context_object_name = "profile"
    model = Publisher

class ProfileDetailView(ProfileViewMixin, DetailView):
    pass

class ProfileUpdateView(ProfileViewMixin, UpdateView):
    pass

# Create your views here.
