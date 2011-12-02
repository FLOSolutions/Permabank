from django.conf.urls.defaults import patterns, include, url
from django_messages.views import compose

from records.views import (CreateWishView, CreateGiftView, WishListView,
        WishDetailView, GiftDetailView, GiftListView, ComposeSuccessView)

urlpatterns = patterns('records.views',
    url(r'^wishes$', WishListView.as_view()),
    url(r'^wishes/add$', CreateWishView.as_view()),
    url(r'^wishes/(?P<slug>[\w-]+)/$', WishListView.as_view(), name='wishlistview'),
    url(r'^wish/(?P<pk>[0-9]+)', WishDetailView.as_view(), name='wishview'),

    url(r'^gifts/add$', CreateGiftView.as_view()),
    url(r'^gift/(?P<pk>[0-9]+)', GiftDetailView.as_view(), name='giftview'),
    url(r'^gifts$', GiftListView.as_view()),
    url(r'^gifts/(?P<slug>[\w-]+)/$', GiftListView.as_view(), name='giftlistview'),

    #(r'^$', ProfileListView.as_view()),
    #(r'^edit/$', UserUpdateView.as_view()),

    url(r'^messages/compose_embedded$', compose,
        {'success_url': '/compose_success',},
        name='messages_compose_embedded'),
    url(r'^compose_success', ComposeSuccessView.as_view()),
)
