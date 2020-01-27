
from django import forms
from .models import CableCalculator


class CableCalculatorForm(forms.ModelForm):
    class Meta:
        model = CableCalculator
        fields = ('instalation','isolation','number_polos', 'corrente_ckt','tension') 
