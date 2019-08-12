from mixer.backend.django import mixer

import pytest

@pytest.mark.django_db
class TestModels:

	def test_stock_name(self):
		stock = mixer.blend('stock.Stock', name='Apple Inc.')
		assert stock.print_name == 'Apple Inc.'

	def test_stock_volatility(self):
		stock = mixer.blend('stock.Market', high=10, low=7)
		assert stock.volatility == 3

	def test_stock_volatility_exception(self):
		stock = mixer.blend('stock.Market',  high=3, low=10)
		with pytest.raises(ValueError, match=r"Volatilty cannot be in negative."):
			stock.volatility