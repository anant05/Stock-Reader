from django.db import models
from apps.stock.behaviors import Nameable, Stockable, Timestampable


class Stock(Nameable, Timestampable):
	ticker = models.CharField(max_length=5)

	def __str__(self):
		return "Share: {}[{}]".format(self.name, self.ticker)

class Analysis(Stockable, Timestampable):
	resistance = models.DecimalField(max_digits=7, decimal_places=2)
	support = models.DecimalField(max_digits=7, decimal_places=2)
	stock_range = models.CharField(max_length=50)
	comments = models.CharField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return "Analysis Component: {} [{}] ".format(self.ticker, self.stock_range)

class Market(Stockable, Timestampable):
	open = models.DecimalField(max_digits=7, decimal_places=2)
	close = models.DecimalField(max_digits=7, decimal_places=2)
	high = models.DecimalField(max_digits=7, decimal_places=2)
	low = models.DecimalField(max_digits=7, decimal_places=2)
	volume = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return "Market [{}] {}".format(self.ticker, self.created_date)