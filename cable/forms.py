
from django import forms
from .models import ResidencDimens, RProject


class ResidencDimensForm(forms.ModelForm):
    class Meta:
        model = ResidencDimens
        fields = (  'r_project','r_local','r_type_circuit','r_tension','r_numbers_points',
                    'r_power_va','r_circuit_length','r_volt_drop_allow','r_numero_polos')


class RProjectForm(forms.ModelForm):
    class Meta:
        model = RProject
        fields = ('r_project','r_description')