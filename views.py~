from django.views.generic import TemplateView

from django.contrib.auth.models import User

from records.models import Wish, Gift

class HomeView(TemplateView):
	
	template_name="home.html"
	
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['gifts'] = Gift.objects.order_by('-created','title').filter(is_featured=True)[:3]
		context['wishes'] = Wish.objects.order_by('-created','title').filter(is_featured=True)[:3]
		return context 