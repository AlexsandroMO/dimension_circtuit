
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ResidencDimens
from .models import RProject
from .forms import ResidencDimensForm
from .forms import RProjectForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import main
from django import db


@login_required
def home(request):
    #db.reset_queries()
    project_name = RProject.objects.all()

    return render(request, 'cable/home.html', {'project_name': project_name})


@login_required
def taskList(request, id):

    read_project = get_object_or_404(RProject, pk=id)
    
    task = ResidencDimens.objects.filter(r_project_id=read_project).order_by('-r_local')
    project_name = RProject.objects.all()

    return render(request, 'cable/lista-circuitos.html', {'task': task, 'project_name': project_name})


@login_required
def newTask(request):

    if request.method == 'POST':
        form = ResidencDimensForm(request.POST)

        task = form.save(commit=False)

        if form.is_valid():

            task = form.save(commit=False)
            task.total_va = (task.potencia_va * task.quant)
            #--------------------------------------------------
            #Dimensiona total de VA
            t_va = str(task.tensa_va)
            #print('\n\n',type(t_va),'\n\n')
            #t_va = float(task.total_va)
            task.corrente_a = round((float(task.total_va) / int(t_va)),3)
        
            #--------------------------------------------------
            #Calcula bitola do cabo
            #cable = main.table_tens(float(task.total_va), task.tensa_va)
            cable = main.calc_cable(str(task.comprimento), task.corrente_a)
            task.sessao_condutor = cable

            print(task.sessao_condutor)
            #--------------------------------------------------
            #Verifica capaciadde de Corrente
            corr = task.sessao_condutor
            test = main.read_sql_corr(corr)

            corrente = test['capacidade_conducao'][0]

            if corrente > float(task.corrente_a):
                task.capacidade_corrente = 'OK'
            else:
                task.capacidade_corrente = 'NÀO'

            #--------------------------------------------------
            #Dimensiona Disjuntos
            disj = main.table_disj(float(task.total_va), task.tensa_va)
            task.corrente_nominal = disj

            cor_nom = int(task.corrente_nominal)
            #--------------------------------------------------
            dj = cor_nom
            test = main.read_sql_dj(dj)
            djj = int(test['dj'][0])

            if djj > (float(task.corrente_a) * 1.1):
                task.verifica_dj = 'OK'
            else:
                task.verifica_dj = 'NÀO'

            #--------------------------------------------------
            id_x = task.projeto
            test = main.read_sql_filter_id(id_x)
            id_project = int(test['id'][0])
            #---------------------------------------------------
            #Verifica Queda de tensão
            queda = task.sessao_condutor
            test = main.read_sql_queda(queda)
            queda_tensao = test['queda_tesao'][0]

            calc = ((((float(queda_tensao) * float(task.corrente_a)) * float(task.comprimento)) / (1000) / int(t_va)))

            task.queda_tensao_ckt = calc * 100
            
            if (float(task.queda_tensao_perm) / 100)< task.queda_tensao_ckt:
                task.queda_tensao_test = 'OK'
            else:
                task.queda_tensao_test = 'NÃO'
            #--------------------------------------------------

            task.save()

            link = '/tasklist'

            url = '{}/{}'.format(link, id_project)
            return redirect(url)

    else:
        form = ResidencDimensForm()
        return render(request, 'cable/add-task.html', {'form': form})


@login_required
def editTask(request, id):

    task = get_object_or_404(ResidencDimens, pk=id)
    form = ResidencDimensForm(instance=task)
    project_name = RProject.objects.all()

    if request.method == 'POST':
        form = ResidencDimensForm(request.POST, instance=task)

        if form.is_valid():

            task = form.save(commit=False)
            task.total_va = (task.potencia_va * task.quant)
            #--------------------------------------------------
            #Dimensiona total de VA
            t_va = str(task.tensa_va)
            #print('\n\n',type(t_va),'\n\n')
            #t_va = float(task.total_va)
            task.corrente_a = round((float(task.total_va) / int(t_va)),3)
        
            #--------------------------------------------------
            #Calcula bitola do cabo
            #cable = main.table_tens(float(task.total_va), task.tensa_va)
            cable = main.calc_cable(str(task.comprimento), task.corrente_a)
            task.sessao_condutor = cable

            print(task.sessao_condutor)
            #--------------------------------------------------
            #Verifica capaciadde de Corrente
            corr = task.sessao_condutor
            test = main.read_sql_corr(corr)

            corrente = test['capacidade_conducao'][0]

            if corrente > float(task.corrente_a):
                task.capacidade_corrente = 'OK'
            else:
                task.capacidade_corrente = 'NÀO'

            #--------------------------------------------------
            #Dimensiona Disjuntos
            disj = main.table_disj(float(task.total_va), task.tensa_va)
            task.corrente_nominal = disj

            cor_nom = int(task.corrente_nominal)
            #--------------------------------------------------
            dj = cor_nom
            test = main.read_sql_dj(dj)
            djj = int(test['dj'][0])

            if djj > (float(task.corrente_a) * 1.1):
                task.verifica_dj = 'OK'
            else:
                task.verifica_dj = 'NÀO'

            #--------------------------------------------------
            id_x = task.projeto
            test = main.read_sql_filter_id(id_x)
            id_project = int(test['id'][0])
            #---------------------------------------------------
            #Verifica Queda de tensão
            queda = task.sessao_condutor
            test = main.read_sql_queda(queda)
            queda_tensao = test['queda_tesao'][0]

            calc = ((((float(queda_tensao) * float(task.corrente_a)) * float(task.comprimento)) / (1000) / int(t_va)))

            task.queda_tensao_ckt = calc * 100
            
            if (float(task.queda_tensao_perm) / 100)< task.queda_tensao_ckt:
                task.queda_tensao_test = 'OK'
            else:
                task.queda_tensao_test = 'NÃO'
            #--------------------------------------------------

            task.save()

            link = '/tasklist'

            url = '{}/{}'.format(link, id_project)
            return redirect(url)

        else:
            return render(request, 'cable/edit-task.html', {'form': form, 'task': task, 'project_name': project_name})

    else:
        return render(request, 'cable/edit-task.html', {'form': form, 'task': task, 'project_name': project_name})


@login_required
def deleteTask(request, id):
    task = get_object_or_404(ResidencDimens, pk=id)

    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    #--------------------------------------------------
    id_x = task.projeto
    test = main.read_sql_filter_id(id_x)
    id_project = int(test['id'][0])
    #--------------------------------------------------

    link = '/tasklist'
    url = '{}/{}'.format(link, id_project)
    return redirect(url)

#------------------------------

@login_required
def newProject(request):

    if request.method == 'POST':
        form = RProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            
            project.save()

            return redirect('/')

    else:
        form = RProjectForm()
        return render(request, 'cable/add-project.html', {'form': form})


@login_required
def editProject(request, id):
    read_project = get_object_or_404(RProject, pk=id)
    form = RProjectForm(instance=read_project)
    project_name = RProject.objects.all()

    form = RProjectForm(instance=read_project)

    if request.method == 'POST':
        form = RProjectForm(request.POST, instance=read_project)

        if form.is_valid():

            read_project.save()

            return redirect('/')

        else:
            return render(request, 'cable/edit-project.html', {'form': form, 'project_name': project_name})

    else:
        return render(request, 'cable/edit-project.html', {'form': form, 'project_name': project_name})


@login_required
def deleteProject(request, id):
    project = get_object_or_404(RProject, pk=id)
    project.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')









def helloworld(request):
    return HttpResponse('Hello World!')


