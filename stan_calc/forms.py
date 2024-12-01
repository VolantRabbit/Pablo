from django import forms

class SumForm(forms.Form):
    number1 = forms.FloatField(label="First Number", required=True)
    number2 = forms.FloatField(label="Second Number", required=True)