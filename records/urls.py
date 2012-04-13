from django.conf.urls.defaults import patterns, include, url
from messaging.views import compose

from records.views import *

urlpatterns = patterns('records.views',
    url(r'^wishes$', WishListView.as_view()),
    url(r'^wishes/add$', CreateWishView.as_view()),
    url(r'^wishes/(?P<slug>[\w-]+)/$', WishListView.as_view(), name='wishlist'),
    url(r'^wish/(?P<pk>[0-9]+)/update', UpdateWishView.as_view()),
    url(r'^wish/(?P<pk>[0-9]+)', WishDetailView.as_view(), name='wish'),

    url(r'^gifts/add$', CreateGiftView.as_view()),
    url(r'^gift/(?P<pk>[0-9]+)/update', UpdateGiftView.as_view()),
    url(r'^gift/(?P<pk>[0-9]+)', GiftDetailView.as_view(), name='gift'),
    url(r'^gifts$', GiftListView.as_view()),
    url(r'^gifts/(?P<slug>[\w-]+)/$', GiftListView.as_view(), name='giftlist'),

    url(r'^thank', CreateThankYouView.as_view()),
    url(r'^welcome', CreateYoureWelcomeView.as_view()),

    # messaging
    url(r'^messages/compose_embedded$', compose,
        {'success_url': '/compose_success',},
        name='messages_compose_embedded'),
    url(r'^compose_success', ComposeSuccessView.as_view()),
)
