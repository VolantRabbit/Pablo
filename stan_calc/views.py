from django.shortcuts import render
from .forms import SumForm  # Import the form
from .eu_scraper import scrape_euro_to_dinar

def calc(request):
    result = None
    scraped_value = None  # Variable to hold the scraped value

    if request.method == 'POST':
        form = SumForm(request.POST)  # Bind the form to POST data
        if form.is_valid():
            num1 = form.cleaned_data['number1']
            num2 = form.cleaned_data['number2']
            result = num1 + num2
        else:
            result = "Invalid input"
    else:
        form = SumForm()  # Create an empty form for GET requests

    # Call the scraper function
    scraped_value = scrape_euro_to_dinar()

    # Add both the form and scraped value to the context
    return render(request, 'stan_calc/calc.html', {
        'form': form,
        'result': result,
        'scraped_value': scraped_value
    })

