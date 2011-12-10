"""
    Permabank URL Mapping
"""
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from views import HomeView

import admin_site
#import notification


urlpatterns = patterns('',
    # home page
	url(r'^$', HomeView.as_view(), name='home'),

    # profiles and authentication
    url(r'^openid/', include('django_openid_auth.urls')),
    # todo: successful logout should add an alert, in the style of flask.flash
    url(r'^logout/$', 'django.contrib.auth.views.logout',
            kwargs={'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^profiles/', include('profiles.urls')),

    # messaging
    (r'^messages/', include('messages.urls')),

    # admin
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),

    # search
    (r'^search/', include('haystack.urls')),

    # notification
    #(r'^notification/', include('notification.urls')),

    # records
    url(r'', include('records.urls')),
)

if settings.DEBUG:
    # when running locally, Django should serve static files
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
