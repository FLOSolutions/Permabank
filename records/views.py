from django.views.generic import CreateView

from records.models import Wish, Gift
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
    template_name = 'add_gift.html'
    sucess_url = '/gifts/%(id)s'

@requires_login
class CreateWishView(UserCreateView):
    model = Wish
    form_class = WishForm
    template_name = 'add_wish.html'
    success_url = '/wishes/%(id)s'

class WishListView(ListView):
    model = Wish
    context_object_name = "wish"
    template_name = "wish_list.html"

class WishDetailView(DetailView):
    model = Wish
    context_object_name = "wish"
    template_name = "wish_details.html"
