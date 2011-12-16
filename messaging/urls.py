from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from permabank.messaging.views import *

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': 'inbox/'}, name='messaging_redirect'),
    url(r'^inbox/$', inbox, name='messaging_inbox'),
    url(r'^outbox/$', outbox, name='messaging_outbox'),
    url(r'^compose/$', compose, name='messaging_compose'),
    url(r'^compose/(?P<recipient>[\w.@+-]+)/$', compose, name='messaging_compose_to'),
    url(r'^reply/(?P<message_id>[\d]+)/$', reply, name='messaging_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', view, name='messaging_detail'),
    url(r'^delete/(?P<message_id>[\d]+)/$', delete, name='messaging_delete'),
    url(r'^undelete/(?P<message_id>[\d]+)/$', undelete, name='messaging_undelete'),
    url(r'^trash/$', trash, name='messaging_trash'),
)
