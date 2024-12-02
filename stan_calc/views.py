from django.shortcuts import render
from .forms import SumForm  # Import the form

def calc(request):
    result = None
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

    return render(request, 'stan_calc/calc.html', {'form': form, 'result': result})