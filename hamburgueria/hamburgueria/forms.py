# forms.py
from django import forms
from .models import Pedido, Pao, Carne, Opcionais

class BurgerForm(forms.ModelForm):
    pao = forms.ModelChoiceField(queryset=Pao.objects.all(), required=True, widget=forms.Select(attrs={'class': 'caixaT'}))
    carne = forms.ModelChoiceField(queryset=Carne.objects.all(), required=True, widget=forms.Select(attrs={'class': 'caixaT'}))
    opcionais = forms.ModelMultipleChoiceField(queryset=Opcionais.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'caixaT'}))
   
    class Meta:
        model = Pedido
        fields = ['nome', 'pao', 'carne', 'opcionais']
