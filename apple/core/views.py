from django.views.generic import TemplateView ,ListView


class HomeView(TemplateView):
	template_name = 'core/home.html'

class AboutView(TemplateView):
	template_name = 'core/about.html'