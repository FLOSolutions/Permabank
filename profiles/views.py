from django.views.generic import DetailView, TemplateView, UpdateView

from profiles.models import Profile
from utils import requires_login

@requires_login
class TestView(TemplateView):
    template_name = "test.html"

class ProfileViewMixin(object):
    context_object_name = "profile"
    model = Profile

@requires_login
class ProfileDetailView(ProfileViewMixin, DetailView):
    pass

class ProfileUpdateView(ProfileViewMixin, UpdateView):
    pass

# Create your views here.
