
from django.contrib import admin
from .models import IsolatioType, InstalatioType, CableCalculator, Tension


class ListaCableCalculator(admin.ModelAdmin):
    list_display = ('instalation','isolation','number_polos', 'corrente_ckt') 
    

admin.site.register(CableCalculator, ListaCableCalculator)
admin.site.register(IsolatioType)
admin.site.register(InstalatioType)
admin.site.register(Tension)

