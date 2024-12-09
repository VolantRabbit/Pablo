from django import forms

class SumForm(forms.Form):
    stan_eur = forms.FloatField(label="Stan EUR", required=True)
    internet = forms.FloatField(label="Internet", required=True)