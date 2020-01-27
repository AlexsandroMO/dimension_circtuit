
from django.contrib import admin
from .models import RTypeCircuit, RTension, RProject, ResidencDimens


class ListResidencDimens(admin.ModelAdmin):
    list_display = (  'r_project','r_local','r_type_circuit','r_tension','r_numbers_points',
                    'r_power_va','r_total_power_va','r_current_a','r_circuit_length','r_conductor_session',
                    'r_volt_drop_allow','r_numero_polos','r_nominal_chain','r_appl_circ_break' )


class ListRProject(admin.ModelAdmin):
    list_display = ('r_project','r_description')
    

admin.site.register(RTypeCircuit)
admin.site.register(RTension)
admin.site.register(RProject, ListRProject)
admin.site.register(ResidencDimens, ListResidencDimens)

