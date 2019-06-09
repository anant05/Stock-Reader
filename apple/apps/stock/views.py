from django.views.generic import TemplateView ,ListView, DetailView
from apps.stock.models import Stock

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class StockListView(ListView):
	model = Stock
	template_name = 'stock/stock_list.html'
	context_object_name = 'stock_objects'

	def head(self, *args, **kwargs):
		last_stock = self.get_queryset().latest('created_date')
		response = HttpResponse('')
		response['Last-Added'] = last_stock.created_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
		return response


class StockDetailView(DetailView):
	model = Stock
	template_name = 'stock/stock_detail.html'

	def get_context_data(self, **kwargs):
		print("this is what you get in life")
		print(kwargs)
		# Call the base implementation first to get a context.
		context = super().get_context_data(**kwargs)
		print("this is the context")
		print(context)
		stock = get_object_or_404(Stock, **kwargs)
		print("this is the stock")
		print(stock)
		print(kwargs)
		return context