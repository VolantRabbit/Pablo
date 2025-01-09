from django import forms

class FlatForm(forms.Form):
    internet = forms.FloatField(label="Internet", required=True)
    electricity = forms.FloatField(label="Electricity", required=True)
    water = forms.FloatField(label="Water", required=True)
    household = forms.FloatField(label="Household", required=True)
