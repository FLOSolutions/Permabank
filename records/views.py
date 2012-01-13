from django.contrib import messages
from django.http import Http404
from django.views.generic import (
        CreateView,
        UpdateView,
        DetailView,
        ListView,
        TemplateView
)

from profiles.models import Profile

from records.models import Wish, Gift, Category
from records.forms import WishForm, GiftForm
from messaging.models import Message

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

class UserUpdateView(UpdateView):
    """ A generic view that attaches the current user to the form"""

    def get_form_kwargs(self):
        """ Attach the current user to the form """
        kwargs = super(UserUpdateView, self).get_form_kwargs()

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

@requires_login
class UpdateGiftView(UserUpdateView):
    model = Gift
    form_class = GiftForm
    template_name = 'records/add_gift.html'
    success_url = '/gift/%(id)s'

@requires_login
class UpdateWishView(UserUpdateView):
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

class RecordMessageMixin(object):
    def post(self, request, *args, **kwargs):
        message_body = self.request.POST.get('body')
        if message_body:
            record = self.get_object()
            message_subject = self.subject_format.format(record.short_title)
            message = Message.objects.create(
                sender=self.request.user,
                recipient=record.user.user,
                record=record,
                body=message_body,
                subject=message_subject
            )
            # add a message to the session
            messages.success(request, 'Your message was sent successfully')
        return self.get(request, *args, **kwargs)

class WishListView(RecordListView):
    model = Wish
    context_object_name = "wishes"
    template_name = "records/wish_list.html"

class WishDetailView(RecordMessageMixin, DetailView):
    model = Wish
    subject_format = '''Your wish for "{}"'''


class GiftListView(RecordListView):
    model = Gift
    context_object_name = "gifts"
    template_name = "records/gift_list.html"

class GiftDetailView(RecordMessageMixin, DetailView):
    model = Gift
    subject_format = '''Your offer of "{}"'''

class ComposeSuccessView(TemplateView):
    """NOTE(matias): django-messages forces a redirect on compose success;
       in our case, we don't want to do anything... so we render this template.
       There may be some way better to do this?"""
    template_name = "records/compose_success.html"
