
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
    project_name = RProject.objects.all().filter(user=request.user)

    return render(request, 'cable/home.html', {'project_name': project_name})


@login_required
def taskList(request, id):

    #tasks_list = Task.objects.all().order_by('-type_task').filter(user=request.user)

    read_project = get_object_or_404(RProject, pk=id)
    
    task = ResidencDimens.objects.filter(r_project_id=read_project, user=request.user).order_by('-r_local')
    project_name = RProject.objects.all().filter(user=request.user)

    return render(request, 'cable/lista-circuitos.html', {'task': task, 'project_name': project_name,'read_project': read_project})


@login_required
def newTask(request):

    project_name = RProject.objects.all().filter(user=request.user)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',project_name[0])
    
    #task = ResidencDimens.objects.filter(user=request.user)
    #print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',task)

    '''
    task = get_object_or_404(ResidencDimens, pk=id)
    task = ResidencDimens.objects.filter(user=request.user)
    form = ResidencDimensForm(instance=task)
    '''
    if request.method == 'POST':
        form = ResidencDimensForm(request.POST)
        #task = ResidencDimens.objects.filter(user=request.user)
        #task = ResidencDimens.objects.filter(user=request.user)
        #print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',form)

        #form = ResidencDimensForm(instance=task)

        if form.is_valid():

            task = form.save(commit=False)

            #---------------------------------------------
            #Potência total do ckt
            task.r_total_power_va = (task.r_numbers_points * task.r_power_va)
            #--------------------------------------------------

            #task.r_nominal_chain = 0
            #Corrente total do circuito
            tension = str(task.r_tension)
            task.r_current_a = round(task.r_total_power_va / (int(tension) - ((int(tension) * task.r_volt_drop_allow) / 100)),2)
            #--------------------------------------------------
            #Bitola do cabo
            cable = main.calc_cable(str(task.r_circuit_length), task.r_current_a, task.r_tension)
            task.r_conductor_session = cable
            #--------------------------------------------------
            #Corrente nomenal do ckt
            disj = main.table_tens(task.r_total_power_va, task.r_tension)
            task.r_nominal_chain = disj
            #--------------------------------------------------
            #Dimensiona Disjuntores
            djj = main.table_disj(task.r_total_power_va, int(tension))
            task.r_appl_circ_break = djj
            #--------------------------------------------------

            #id_name = main.read_sql_proj_id(task.r_project)
            #id_name = id_name['id'][0]

            #read_project = get_object_or_404(RProject, pk=id_name)
            #task.r_project = project_name[0]

            task.user = request.user

            task.save()

            #--------------------------------------------------
            id_x = task.r_project
            test = main.read_sql_filter_id(id_x)
            id_project = int(test['id'][0])
            #---------------------------------------------------

            link = '/tasklist'

            url = '{}/{}'.format(link, id_project)
            return redirect(url)

    else:
        form = ResidencDimensForm()
        return render(request, 'cable/add-task.html', {'form': form, 'project_name': project_name})


@login_required
def editTask(request, id):

    task = get_object_or_404(ResidencDimens, pk=id)
    form = ResidencDimensForm(instance=task)

    project_name = RProject.objects.all().filter(user=request.user)

    if request.method == 'POST':
        form = ResidencDimensForm(request.POST, instance=task)

        if form.is_valid():
            #---------------------------------------------
            #Potência total do ckt
            task.r_total_power_va = (task.r_numbers_points * task.r_power_va)
            #--------------------------------------------------
            #Corrente total do circuito
            tension = str(task.r_tension)
            #task.r_current_a = round(task.r_total_power_va / int(tension),2)
            task.r_current_a = round(task.r_total_power_va / (int(tension) - ((int(tension) * task.r_volt_drop_allow) / 100)),2)
            #--------------------------------------------------
            #Bitola do cabo
            cable = main.calc_cable(str(task.r_circuit_length), task.r_current_a, task.r_tension)
            task.r_conductor_session = cable
            #--------------------------------------------------
            #Corrente nomenal do ckt
            disj = main.table_tens(task.r_total_power_va, task.r_tension)
            task.r_nominal_chain = disj
            #--------------------------------------------------
            #Dimensiona Disjuntores
            djj = main.table_disj(task.r_total_power_va, int(tension))
            task.r_appl_circ_break = djj
            #--------------------------------------------------

            id_name = main.read_sql_proj_id(task.r_project)
            id_name = id_name['id'][0]

            read_project = get_object_or_404(RProject, pk=id_name)
            task.r_project = read_project

            task.user = request.user

            task.save()

            #--------------------------------------------------
            id_x = task.r_project
            test = main.read_sql_filter_id(id_x)
            id_project = int(test['id'][0])
            #---------------------------------------------------

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
    id_x = task.r_project
    test = main.read_sql_filter_id(id_x)
    id_project = int(test['id'][0])
    #--------------------------------------------------

    link = '/tasklist'
    url = '{}/{}'.format(link, id_project)
    return redirect(url)

#------------------------------

@login_required
def newProject(request):

    user = request.user
    ss = main.read_sql_user_name(user)
    id_user = ss.username[0]

    if request.method == 'POST':
        form = RProjectForm(request.POST)
        task = form.save(commit=False)

        if form.is_valid():
            project = form.save(commit=False)

            task.user = request.user 
            
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


