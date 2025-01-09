from django.shortcuts import render
from .forms import FlatForm
import requests


def get_exchange_rates():
    currency_code = "eur"
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    response = requests.get(url)
    data = response.json()
    eur_rate = data.get("rsd", {}).get("rate", None)
    return eur_rate


def euro_rate(request):
    return get_exchange_rates()


def flat_cost(request):
    stan_eur = 190
    stan_cost_din = None

    if request.method == 'POST' and 'flat_form_btn' in request.POST:
        eur_rate_value = euro_rate(request)
        if eur_rate_value:
            stan_cost_din = round(eur_rate_value * stan_eur, 2)

    return stan_cost_din

def payments(request):
    form = FlatForm()
    sum_payments = None
    if request.method == 'POST':
        form = FlatForm(request.POST)
        if form.is_valid():
            sum_payments = (
                form.cleaned_data['internet'] +
                form.cleaned_data['electricity'] +
                form.cleaned_data['water'] +
                form.cleaned_data['household']
            )
        else:

            for field_name in form.errors:
                form.errors[field_name] = [
                    error for error in form.errors[field_name]
                    if error != 'This field is required.'
                ]
    return form, sum_payments

def render_flat(request):
    eur_rate = euro_rate(request)
    stan_cost_din = flat_cost(request)
    form_payments, sum_payments = payments(request)

    return render(request, 'stan_calc/calc.html', {
        'eur_rate': eur_rate,
        'stan_cost_din': stan_cost_din,
        'form_payments': form_payments,
        'sum_payments': sum_payments,
    })


