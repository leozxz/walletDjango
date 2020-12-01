from django import forms

class TransacaoForm(forms.Form):
    real = forms.DecimalField(max_digits=9, decimal_places=2)
    cripto = forms.DecimalField(max_digits=9, decimal_places=2)
