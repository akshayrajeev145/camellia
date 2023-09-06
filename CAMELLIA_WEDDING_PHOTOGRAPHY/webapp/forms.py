from django import forms

class MyForm(forms.Form):
    required_field = forms.CharField(label='Required Field', required=True)
