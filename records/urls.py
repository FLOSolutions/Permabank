from django.conf.urls.defaults import patterns, include

from records.views import CreateWishView

urlpatterns = patterns('records.views',
    #(r'^wishes$', WishListView.as_view()),
    (r'^wishes/add$', CreateWishView.as_view()),
    #(r'^$', ProfileListView.as_view()),
    #(r'^(?P<pk>[0-9]+)', ProfileDetailView.as_view()),
    #(r'^edit/$', UserUpdateView.as_view()),
)
