import requests
from django.shortcuts import render

def get_exchange_rates():
    currency_code = "eur"
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    response = requests.get(url)
    data = response.json()
    eur_rate = data.get("rsd", {}).get("rate", None)
    return eur_rate
def calc(request):
    eur_rate = None
    if request.method == 'POST':
        eur_rate = get_exchange_rates()  # Get the EUR rate on button click
    return render(request, 'stan_calc/calc.html', {'eur_rate': eur_rate})


