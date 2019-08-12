from django.urls import reverse, resolve

class TestUrls:

	def test_stock_list_url(self):
		path = reverse('stock:List')
		print(path)
		print(resolve(path).view_name)
		assert resolve(path).view_name == 'stock:List'

	def test_stock_detail_url(self):
		path = reverse('stock:detail', kwargs={'pk': '1'})
		assert resolve(path).view_name == 'stock:detail'