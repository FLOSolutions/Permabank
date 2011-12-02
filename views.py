from django.views.generic import TemplateView
from django.contrib.auth.models import User

from records.models import Wish, Gift

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """Get featured gifts and wishes"""
        gifts = Gift.objects.filter(is_featured=True).order_by('-created')[:3]
        wishes = Wish.objects.filter(is_featured=True).order_by('-created')[:3]
        return {'gifts': gifts, 'wishes': wishes}
