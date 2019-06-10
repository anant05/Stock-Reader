from django.db import models
from apps.stock.behaviors import Nameable, Stockable, Timestampable

from django.urls import reverse

class Stock(Nameable, Timestampable):
	ticker = models.CharField(max_length=5)

	def __str__(self):
		return "Share: {}[{}]".format(self.name, self.ticker)

	def get_absolute_url(self):
		return reverse("stock:detail", kwargs={"pk": self.id})

	def get_list_url(self):
		return reverse("stock:List")

class Analysis(Stockable, Timestampable):
	BEAR = 'Bearish'
	BULL = 'Bullish'
	SIDEWAYS = 'sideways'
	stock_stance = [
		(BEAR, 'Bearish'),
		(BULL, 'Bullish'),
		(SIDEWAYS, 'Neutral')
	]

	priority_trade = [
		(1, 'Highly Interested'),
		(2, 'Interested'),
		(3, 'Wait'),
		(4, 'Risk')
	]

	resistance = models.DecimalField(max_digits=7, decimal_places=2)
	support = models.DecimalField(max_digits=7, decimal_places=2)
	stock_range = models.CharField(max_length=50)
	comments = models.CharField(max_length=1000, blank=True, null=True)
	stance = models.CharField(max_length=10, choices=stock_stance, default=SIDEWAYS)
	priority = models.IntegerField(choices=priority_trade, default=3)

	def __str__(self):
		return "Analysis Component: {} [{}] ".format(self.ticker, self.stock_range)

	def get_absolute_url(self):
		return reverse("stock:notes")

class Market(Stockable, Timestampable):
	open = models.DecimalField(max_digits=7, decimal_places=2)
	close = models.DecimalField(max_digits=7, decimal_places=2)
	high = models.DecimalField(max_digits=7, decimal_places=2)
	low = models.DecimalField(max_digits=7, decimal_places=2)
	volume = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return "Market [{}] {}".format(self.ticker, self.created_date)
