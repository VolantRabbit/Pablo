from django.shortcuts import render
from .forms import SumForm  # Import the form


def calc(request):

    return render(request, 'stan_calc/calc.html', )
