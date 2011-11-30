from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from permabank.views import (HomeView)

import django_messages

import admin_site


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
	url(r'^$', HomeView.as_view()),
    url(r'^about$', TemplateView.as_view(template_name='about.html'),
        name='about'),

    #url(r'^$', 'epio_skel.views.home', name='home'),
    # url(r'^epio_skel/', include('epio_skel.foo.urls')),

    # profiles and authentication
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^profiles/', include('profiles.urls')),

    # messaging
    (r'^messages/', include('django_messages.urls')),

    # admin
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'', include('records.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
