from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.converter, name='converter'),
    path('convert/', views.convert_currency, name='convert_currency'),
    path('rates/', views.exchange_rates, name='exchange_rates'),
    path('update-rate/', views.update_exchange_rate, name='update_exchange_rate'),
    path('history/', views.conversion_history, name='conversion_history'),
]