
from django.db import models
from django.contrib.auth import get_user_model


class RTypeCircuit(models.Model):
    r_ckt = models.CharField(verbose_name='Tipo de Circuito', max_length=50)

    def __str__(self):
        return self.r_ckt


class RTension(models.Model):
    r_volts = models.CharField(max_length=10)

    def __str__(self):
        return self.r_volts 


class RProject(models.Model):
    r_project = models.CharField(verbose_name='Nome do Projeto', max_length=100)
    r_description = models.TextField(verbose_name='Descrição do Projeto', blank=True, null=False)
    r_create_project = models.DateTimeField(auto_now_add=True)
    r_update_project = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.r_project


class ResidencDimens(models.Model):
    r_project = models.ForeignKey(RProject, verbose_name='Nome do Projeto', on_delete=models.CASCADE)
    r_local = models.CharField(verbose_name='Local da Instalação', max_length=50)
    r_type_circuit = models.ForeignKey(RTypeCircuit, verbose_name='Tipo de Instalação', on_delete=models.CASCADE)
    r_tension = models.ForeignKey(RTension, verbose_name='Tensão (VA)', on_delete=models.CASCADE)
    r_numbers_points = models.IntegerField(verbose_name='Quantidade')
    r_power_va = models.FloatField(verbose_name='Potência (VA)')
    r_total_power_va = models.FloatField(verbose_name='Total (VA)', blank=True)
    r_current_a = models.FloatField(verbose_name='Corrente (A)', blank=True)
    r_circuit_length = models.IntegerField(verbose_name='Comprimento do Circuito (m)')
    r_conductor_session = models.CharField(verbose_name='Sessão Transversal do Condutor (mm²)', max_length=4, blank=True)
    r_volt_drop_allow = models.FloatField(verbose_name='Queda de Tensão Permitida (%)')
    r_numero_polos = models.IntegerField(verbose_name='Número de Polos')
    r_nominal_chain = models.FloatField(verbose_name='Corrente Nominal', blank=True)
    r_appl_circ_break = models.CharField(verbose_name='Verifica Disjuntor', max_length=3, blank=True)
    r_create_circuit = models.DateTimeField(auto_now_add=True)
    r_update_circuit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.r_local





'''        
class CableCalculator(models.Model):
    tesion = models.ForeignKey(Tensao, verbose_name='Tensão (VA)', blank=True, on_delete=models.CASCADE)
    sessao_condutor = models.ForeignKey(TabelaCondutor, verbose_name='Sessão Transversal do Condutor (mm²)', blank=True, on_delete=models.CASCADE)
    corrente_nominal = models.ForeignKey(Disjuntor, verbose_name='Corrente Nominal', on_delete=models.CASCADE)
    numero_polos = models.DecimalField(verbose_name='Número de Polos', max_digits=4, decimal_places=0, blank=True)
    numero_polos = models.DecimalField(verbose_name='Número de Polos', max_digits=4, decimal_places=0, blank=True)
    capacidade_corrente = models.CharField(verbose_name='Capacidade de Corrente', max_length=3, blank=True)
    
    def __str__(self):
        return self.tesion
'''

