from django.db import models
from django.contrib.auth.models import User

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.code} - {self.name}"

class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_rates')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_rates')
    rate = models.DecimalField(max_digits=20, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('from_currency', 'to_currency', 'user')

    def __str__(self):
        return f"{self.from_currency.code} to {self.to_currency.code}: {self.rate}"

class ConversionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_conversions')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_conversions')
    amount = models.DecimalField(max_digits=20, decimal_places=6)
    converted_amount = models.DecimalField(max_digits=20, decimal_places=6)
    rate_used = models.DecimalField(max_digits=20, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.from_currency.code} to {self.converted_amount} {self.to_currency.code}"