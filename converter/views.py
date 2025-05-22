from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Currency, ExchangeRate, ConversionHistory
from decimal import Decimal

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('converter')
    else:
        form = UserCreationForm()
    return render(request, 'converter/register.html', {'form': form})

@login_required
def converter(request):
    currencies = Currency.objects.all()
    return render(request, 'converter/converter.html', {'currencies': currencies})

@login_required
@require_POST
def convert_currency(request):
    try:
        amount = Decimal(request.POST.get('amount', 0))
        from_currency_id = request.POST.get('from_currency')
        to_currency_id = request.POST.get('to_currency')

        from_currency = Currency.objects.get(id=from_currency_id)
        to_currency = Currency.objects.get(id=to_currency_id)

        try:
            rate = ExchangeRate.objects.get(
                from_currency=from_currency,
                to_currency=to_currency,
                user=request.user
            ).rate
        except ExchangeRate.DoesNotExist:
            try:
                rate = ExchangeRate.objects.get(
                    from_currency=from_currency,
                    to_currency=to_currency,
                    user=None
                ).rate
            except ExchangeRate.DoesNotExist:
                return JsonResponse({'error': 'Exchange rate not found'}, status=400)

        converted_amount = amount * rate

        ConversionHistory.objects.create(
            user=request.user,
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
            converted_amount=converted_amount,
            rate_used=rate
        )

        return JsonResponse({
            'converted_amount': str(converted_amount),
            'rate': str(rate)
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@login_required
def exchange_rates(request):
    rates = ExchangeRate.objects.filter(user=request.user) | ExchangeRate.objects.filter(user=None)
    currencies = Currency.objects.all()
    return render(request, 'converter/exchange_rates.html', {'rates': rates, 'currencies': currencies})

@login_required
@require_POST
def update_exchange_rate(request):
    try:
        from_currency_id = request.POST.get('from_currency')
        to_currency_id = request.POST.get('to_currency')
        rate = Decimal(request.POST.get('rate'))

        from_currency = Currency.objects.get(id=from_currency_id)
        to_currency = Currency.objects.get(id=to_currency_id)

        ExchangeRate.objects.update_or_create(
            from_currency=from_currency,
            to_currency=to_currency,
            user=request.user,
            defaults={'rate': rate}
        )

        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@login_required
def conversion_history(request):
    history = ConversionHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'converter/history.html', {'history': history})