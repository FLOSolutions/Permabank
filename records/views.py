from django.views.generic import (CreateView, ListView, DetailView,
        TemplateView)

from django.http import Http404
from profiles.models import Profile

from permabank.records.models import Wish, Gift, Category
from permabank.records.forms import WishForm, GiftForm
from permabank.messages.models import Message

from utils import requires_login

class UserCreateView(CreateView):
    """ A generic view that attaches the current user to the form """

    # Should form fields be pre-populated with data from query string?
    initial_data_from_query = True

    def get_form_kwargs(self):
        """ Attach the current user to the form """
        kwargs = super(UserCreateView, self).get_form_kwargs()

        # Pre-populate form fields with query params
        if self.initial_data_from_query:
            kwargs['initial'] = self.request.REQUEST

        # Attach user
        if self.request.method in ('POST', 'PUT'):
            kwargs['user'] = self.request.user.profile

        return kwargs

@requires_login
class CreateGiftView(UserCreateView):
    model = Gift
    form_class = GiftForm
    template_name = 'records/add_gift.html'
    success_url = '/gift/%(id)s'

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

    def post(self, request, *args, **kwargs):
        message_body = self.request.POST.get('body')
        if message_body:
            record = self.get_object()
            message_subject = 'Your wish for "{offer}"'.format(
                    offer=record.short_title)
            message = Message.objects.create(
                sender=self.request.user,
                recipient=record.user.user,
                record=record,
                body=message_body,
                subject=message_subject
            )
            # todo: handle notifications and messages?
        return self.get(request, *args, **kwargs)

    #def get_context_data(self, **kwargs):
    #    context = super(WishDetailView, self).get_context_data(**kwargs)
    #    context['form'] = RecordMessageForm()
    #    return context


class GiftListView(RecordListView):
    model = Gift
    context_object_name = "gifts"
    template_name = "records/gift_list.html"

class GiftDetailView(DetailView):
    model = Gift

class ComposeSuccessView(TemplateView):
    """NOTE(matias): django-messages forces a redirect on compose success;
       in our case, we don't want to do anything... so we render this template.
       There may be some way better to do this?"""
    template_name = "records/compose_success.html"
