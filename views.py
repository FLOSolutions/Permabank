from django.views.generic import TemplateView
from django.contrib.auth.models import User

from records.models import Wish, Gift

class HomeView(TemplateView):
    template_name = "home.html"
    num_featured = 3  # num. of items to showcase

    def get_context_data(self, **kwargs):
        """Get featured gifts and wishes"""
        return {
            'gifts': Gift.featured.all()[:self.num_featured],
            'wishes': Wish.featured.all()[:self.num_featured]
        }
