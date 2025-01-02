from django.shortcuts import render
from .forms import SumForm  # Import the form
from .eu_scraper import scrape_euro_to_dinar

def calc(request):
    result = None
    result1 = None
    scraped_value = None  # Variable to hold the scraped value

    # Initialize the form variable outside of the POST condition
    form = SumForm()  # Default form initialization for GET requests

    if request.method == 'POST' and 'act' in request.POST:
        action = request.POST['action']
        if action == 'add':
            form = SumForm(request.POST)  # Bind the form to POST data for "Add" action
            if form.is_valid():
                num1 = form.cleaned_data['stan_eur']  # Get first number
                num2 = form.cleaned_data['internet']   # Get second number
                result1 = num1 + num2  # Perform addition
            else:
                result = "Invalid input"  # Invalid input if form is not valid
        elif action == 'show':
            scraped_value = scrape_euro_to_dinar()  # Call the scraping function
            result = f"Eur/Din rate: {scraped_value}"  # Display scraped value

    return render(request, 'stan_calc/calc.html', {
        'form': form,
        'result': result,
        'result1': result1,
        'scraped_value': scraped_value,
    })
