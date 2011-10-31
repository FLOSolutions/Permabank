from django.conf.urls.defaults import *
from profiles.views import TestView

urlpatterns = patterns('profiles.views',
    (r'^$', TestView.as_view()),
)


"""
urlpatterns = patterns('',
                       url(r'^create/$',
                           views.create_profile,
                           name='profiles_create_profile'),
                       url(r'^edit/$',
                           views.edit_profile,
                           name='profiles_edit_profile'),
                       url(r'^(?P<username>\w+)/$',
                           views.profile_detail,
                           name='profiles_profile_detail'),
                       url(r'^$',
                           views.profile_list,
                           name='profiles_profile_list'),
                       )
"""
