from django.shortcuts import render
from .forms import FlatForm
import requests


def get_exchange_rate(request):
    currency_code = "eur"
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    response = requests.get(url)
    data = response.json()
    eur_rate = data.get("rsd", {}).get("rate", None)
    return round(eur_rate, 2)


def flat_cost(request):
    stan_eur = 190
    eur_rate_value = get_exchange_rate(request)
    stan_cost_din = eur_rate_value * stan_eur
    return stan_cost_din


def payments(request):
    form = FlatForm()
    sum_payments = None
    sum_sum = None
    if request.method == 'POST':
        form = FlatForm(request.POST)
        if form.is_valid():
            sum_payments = (
                form.cleaned_data['internet'] +
                form.cleaned_data['electricity'] +
                form.cleaned_data['water'] +
                form.cleaned_data['household']
            )
            sum_sum = sum_payments + flat_cost(request)
        else:
            for field_name in form.errors:
                form.errors[field_name] = [
                    error for error in form.errors[field_name]
                    if error != 'This field is required.'
                ]
    return form, sum_payments, sum_sum

def render_flat(request):
    eur_rate = get_exchange_rate(request)
    stan_cost_din = flat_cost(request)
    form_payments, sum_payments, sum_sum = payments(request)

    return render(request, 'stan_calc/calc.html', {
        'eur_rate': eur_rate,
        'stan_cost_din': stan_cost_din,
        'form_payments': form_payments,
        'sum_payments': sum_payments,
        'sum_sum': sum_sum,
    })



