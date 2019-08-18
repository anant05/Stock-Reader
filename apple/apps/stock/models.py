from django.db import models
from django.db.models.signals import pre_save

from apps.stock.behaviors import Nameable, Stockable, Timestampable
from django.urls import reverse
import math

from django.utils.text import slugify


class Stock(Nameable, Timestampable):
	ticker = models.CharField(max_length=5)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return "Share: {}[{}]".format(self.name, self.ticker)

	def get_absolute_url(self):
		return reverse("stock:detail", kwargs={"pk": self.id})

	def get_list_url(self):
		return reverse("stock:List")

	@property
	def print_name(self):
		return self.name

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

	def rating(self):
		return math.ceil(self.close)


class Market(Stockable, Timestampable):
	open = models.DecimalField(max_digits=7, decimal_places=2)
	close = models.DecimalField(max_digits=7, decimal_places=2)
	high = models.DecimalField(max_digits=7, decimal_places=2)
	low = models.DecimalField(max_digits=7, decimal_places=2)
	volume = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return "Market [{}] {}".format(self.ticker, self.created_date)

	@property
	def volatility(self):
		_volatility = self.high - self.low
		if _volatility > 0:
			return _volatility
		else:
			raise ValueError('Volatilty cannot be in negative.')

	def change(self):
		return self.open - self.close


def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug in not None:
		slug = new_slug
	exists = Stock.objects.filter(slug=slug).order_by("-id").exist()
	if exists:
		new_slug = "{}-{}".format(slug, instance.id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Stock)