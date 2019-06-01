from django.views.generic import TemplateView ,ListView


class StockView(TemplateView):
	template_name = 'stock/list_view.html'