
from django.db import models
from django.contrib.auth import get_user_model


class IsolatioType(models.Model):
    type_isolation = models.CharField(verbose_name='Tipo de Isolação', max_length=3)

    def __str__(self):
        return self.type_isolation

class InstalatioType(models.Model):
    type_instalation = models.CharField(verbose_name='Tipo de Instalação', max_length=30)

    def __str__(self):
        return self.type_instalation

class Tension(models.Model):
    type_tension = models.CharField(verbose_name='Tipo de Tenção', max_length=4)

    def __str__(self):
        return self.type_tension


class CableCalculator(models.Model):
    instalation = models.ForeignKey(InstalatioType, verbose_name='Tipo de Instalação', blank=True, on_delete=models.CASCADE)
    isolation = models.ForeignKey(IsolatioType, verbose_name='Tipo de Isolação', blank=True, on_delete=models.CASCADE)
    number_polos = models.DecimalField(verbose_name='Número de Polos', max_digits=4, decimal_places=0, blank=True)
    corrente_ckt = models.DecimalField(verbose_name='Potência do CKT', max_digits=4, decimal_places=0, blank=True)
    tension = models.ForeignKey(Tension, verbose_name='Tipo de Tensão', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.instalation





'''class CableCalculator(models.Model):
    tesion = models.ForeignKey(Tensao, verbose_name='Tensão (VA)', blank=True, on_delete=models.CASCADE)
    sessao_condutor = models.ForeignKey(TabelaCondutor, verbose_name='Sessão Transversal do Condutor (mm²)', blank=True, on_delete=models.CASCADE)
    corrente_nominal = models.ForeignKey(Disjuntor, verbose_name='Corrente Nominal', on_delete=models.CASCADE)
    numero_polos = models.DecimalField(verbose_name='Número de Polos', max_digits=4, decimal_places=0, blank=True)
    numero_polos = models.DecimalField(verbose_name='Número de Polos', max_digits=4, decimal_places=0, blank=True)
    capacidade_corrente = models.CharField(verbose_name='Capacidade de Corrente', max_length=3, blank=True)
    
    def __str__(self):
        return self.tesion'''