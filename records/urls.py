from django.conf.urls.defaults import patterns, include

from records.views import (CreateWishView, CreateGiftView, WishListView,
        WishDetailView)

urlpatterns = patterns('records.views',
    #(r'^wishes$', WishListView.as_view()),
    (r'^wishes/add$', CreateWishView.as_view()),
    (r'^wishes/(?P<slug>[\w-]+)/$', WishListView.as_view()),
    (r'^wish/(?P<pk>[0-9]+)', WishDetailView.as_view()),


    (r'^gifts/add$', CreateGiftView.as_view()),
    #(r'^$', ProfileListView.as_view()),
    #(r'^edit/$', UserUpdateView.as_view()),
)
