from django.conf.urls.defaults import *
from profiles.views import (TestView, UserUpdateView, ProfileDetailView,
    ProfileListView)

urlpatterns = patterns('profiles.views',
    url(r'^$', ProfileListView.as_view()),
    url(r'^(?P<pk>[0-9]+)', ProfileDetailView.as_view(), name='profileview'),
    url(r'^edit/$', UserUpdateView.as_view()),
)
