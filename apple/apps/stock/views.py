from django.views.generic import TemplateView ,ListView
from apps.stock.models import Stock

from django.shortcuts import get_object_or_404
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class StockListView(ListView):
	model = Stock
	template_name = 'stock/stock_list.html'

