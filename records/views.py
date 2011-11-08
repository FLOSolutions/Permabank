from django.views.generic import CreateView

from records.models import Wish
from records.forms import WishForm

from utils import requires_login

class UserCreateView(CreateView):
    """ A generic view that attaches the current user to the form """
    def get_form_kwargs(self):
        """ Attach the current user to the form """
        kwargs = super(CreateWishView, self).get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            kwargs['user'] = self.request.user.profile
        return kwargs

@requires_login
class CreateWishView(UserCreateView):
    model = Wish
    form_class = WishForm
    template_name = 'add_wish.html'
    success_url = '/wishes/%(id)s'
