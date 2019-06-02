from django.views.generic import TemplateView ,ListView


class StockView(TemplateView):
	template_name = 'stock/stock_list.html'