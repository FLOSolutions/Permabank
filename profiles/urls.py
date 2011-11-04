from django.conf.urls.defaults import *
from profiles.views import (TestView, UserUpdateView, ProfileDetailView,
    ProfileListView)

urlpatterns = patterns('profiles.views',
    (r'^$', ProfileListView.as_view()),
    (r'^(?P<pk>[0-9]+)', ProfileDetailView.as_view()),
    (r'^edit/$', UserUpdateView.as_view()),
)
