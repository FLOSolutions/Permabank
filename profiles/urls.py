from django.conf.urls.defaults import *
from profiles.views import *

urlpatterns = patterns('profiles.views',
    url(r'^$', ProfileListView.as_view()),
    #url(r'^(?P<profile_id>[0-9]+)/records', profile_records),
    url(r'^(?P<profile_id>[0-9]+)/records', ProfileRecordsView.as_view(), name='profile_records'),
    url(r'^(?P<pk>[0-9]+)$', ProfileDetailView.as_view(), name='profile'),
    url(r'^edit/$', UserUpdateView.as_view()),
)
