from django.contrib import admin
from .models import Currency, ExchangeRate, ConversionHistory

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol')
    search_fields = ('code', 'name')

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('from_currency', 'to_currency', 'rate', 'last_updated', 'user')
    list_filter = ('user',)
    search_fields = ('from_currency__code', 'to_currency__code')

@admin.register(ConversionHistory)
class ConversionHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'from_currency', 'to_currency', 'amount', 'converted_amount', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'from_currency__code', 'to_currency__code')