from django.views.generic import CreateView, ListView, DetailView

from django.http import Http404

from records.models import Wish, Gift, Category
from records.forms import WishForm, GiftForm

from utils import requires_login

class UserCreateView(CreateView):
    """ A generic view that attaches the current user to the form """
    def get_form_kwargs(self):
        """ Attach the current user to the form """
        kwargs = super(UserCreateView, self).get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            kwargs['user'] = self.request.user.profile
        return kwargs

@requires_login
class CreateGiftView(UserCreateView):
    model = Gift
    form_class = GiftForm
    template_name = 'records/add_gift.html'
    sucess_url = '/gifts/%(id)s'

@requires_login
class CreateWishView(UserCreateView):
    model = Wish
    form_class = WishForm
    template_name = 'records/add_wish.html'
    success_url = '/wish/%(id)s'

class RecordListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if not slug or slug == 'all':
            return self.model.objects.order_by('-created')
        else:
            try:
                category = Category.objects.only('id').get(slug=slug)
            except Category.DoesNotExist:
                raise Http404
            return self.model.objects.filter(category=category).order_by(
                    '-created')

class WishListView(RecordListView):
    model = Wish
    context_object_name = "wishes"
    template_name = "records/wish_list.html"

class WishDetailView(DetailView):
    model = Wish
    context_object_name = "wish"
    template_name = "records/wish_details.html"
