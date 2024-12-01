from django.shortcuts import render

def calc(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            result = num1 + num2
        except ValueError:
            result = "Invalid input"
    return render(request, 'stan_calc/calc.html', {'result': result})
