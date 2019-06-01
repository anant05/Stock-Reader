from django.contrib import admin
from apps.stock.models import Stock, Analysis, Market

@admin.register(Stock, Analysis, Market)
class StockAdmin(admin.ModelAdmin):
	pass