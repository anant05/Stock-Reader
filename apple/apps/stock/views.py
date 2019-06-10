from django.views.generic import TemplateView ,ListView, DetailView
from apps.stock.models import Stock, Analysis

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils import CurrentDateTime
import pandas_datareader.data as web


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
		# Call the base implementation first to get a context.
		context = super().get_context_data(**kwargs)
		start = CurrentDateTime().week_ago_datetime
		end = CurrentDateTime().today
		stock_info = web.DataReader(context['stock'].ticker, 'yahoo', start, end)
		s_high, s_low, s_open, _, s_vol, s_price = stock_info.iloc[stock_info.index.argmax()]
		context['stock_info'] = {
			'high': s_high,
			'low': s_low,
			'close': s_price,
			'volume': s_vol,
			'open': s_open
		}
		context['notes'] = Analysis.objects.filter(ticker=kwargs['object'])
		return context



class StockNotesView(ListView):
	model = Analysis
	template_name = 'stock/stock_notes.html'
	context_object_name = 'notes_object'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context.
		context = super().get_context_data(**kwargs)
		context['var'] = 'Bullish'
		print(context)
		return context