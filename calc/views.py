
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
#from django.core.urlresolvers import reverse
from .models import CableCalculator
from .forms import CableCalculatorForm
import main
from django import db


def homecalc(request):

    if request.method == 'POST':
        form = request.POST

        install = float(form['instal'])
        isola = form['isola']
        polo = form['polo']
        corr = form['corr']
        tens = form['tens']

        '''print('\n\n')
        print(install)
        print(isola)
        print(polo)
        print(corr)
        print(tens)

        print(type(install))

        print('\n\n')'''

        #if form.is_valid():
            #task = form.save(commit=False)
            #print('ok')

    return render(request, 'calc/homecalc.html')#, {'project': project})

def newCalc(request):

    if request.method == 'POST':
        form = CableCalculatorForm(request.POST)

        if form.is_valid():
            calc = form.save(commit=False)
            #task.total_va = (task.potencia_va * task.quant)
            #--------------------------------------------------
            '''print('\n\n')
            print('Aqui....')
            print(calc.instalation)
            print(calc.isolation)
            print(calc.number_polos)
            print(calc.corrente_ckt)
            print('hhh {}'.format(calc.tension))
            print('\n\n')'''

            T = '{}'.format(calc.tension)

            calc_result = main.table_calc(float(calc.corrente_ckt), float(T))

            result = []
            for a in calc_result['Cable']:
                result.append(a)

            texto_result = '{} mm²'.format(result[0])

            #form = CableCalculatorForm()

            print(texto_result)

            return render(request, 'calc/new-calc.html', {'form': form, 'texto_result': texto_result})
  
    else:
        form = CableCalculatorForm()
        texto_result = ''
        return render(request, 'calc/new-calc.html', {'form': form, 'texto_result': texto_result})







#=------------------------------------

'''
def newCalc(request):

    if request.method == 'POST':
        form = CableCalculatorForm(request.POST)

        if form.is_valid():
            calc = form.save(commit=False)
            #task.total_va = (task.potencia_va * task.quant)
            #--------------------------------------------------
            print('\n\n')
            print('Aqui....')
            print(calc.instalation)
            print(calc.isolation)
            print(calc.number_polos)
            print(calc.corrente_ckt)
            print('\n\n')

            result = (float(calc.number_polos) * float(calc.corrente_ckt))

            #result = (float(calc.number_polos) * float(calc.corrente_ckt))

            form = CableCalculatorForm()
            
            return render(request, 'calc/new-calc.html', {'form': form, 'result': result})
  
    else:
        form = CableCalculatorForm()
        result = ''
        return render(request, 'calc/new-calc.html', {'form': form, 'result': result})
'''


#======================================





'''
def newCalcResult(request, id):

    if request.method == 'POST':
        form = CableCalculatorForm(request.POST)

        if form.is_valid():
            calc = form.save(commit=False)
            #task.total_va = (task.potencia_va * task.quant)
            #--------------------------------------------------
            print('\n\n')
            print('Aqui....')
            print(calc.instalation)
            print(calc.isolation)
            print(calc.number_polos)
            print(calc.corrente_ckt)
            print('\n\n')

            result = (float(calc.number_polos) * float(calc.corrente_ckt))

            return redirect('new-calc')

    else:
        form = CableCalculatorForm()
        result = ''
        return render(request, 'calc/new-calc.html', {'form': form, 'result': result})


#Manual:

def homecalc(request):

    if request.method == 'POST':
        form = request.POST

        install = float(form['instal'])
        isola = form['isola']
        polo = form['polo']
        corr = form['corr']

        print('\n\n')
        print(install)
        print(isola)
        print(polo)
        print(corr)

        print(type(install))

        print('\n\n')

        #if form.is_valid():
            #task = form.save(commit=False)
            #print('ok')

    return render(request, 'calc/homecalc.html')#, {'project': project})'''
