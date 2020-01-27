
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasklist/<int:id>', views.taskList, name='task-list'),
    path('newtask/', views.newTask, name='new-task'),
    path('edittask/<int:id>', views.editTask, name='edit-task'),
    path('deletetask/<int:id>', views.deleteTask, name='delete-task'),

    path('newproject/', views.newProject, name='new-project'),
    path('editproject/<int:id>', views.editProject, name='edit-project'),
    path('deleteproject/<int:id>', views.deleteProject, name='delete-project'),

    #path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    #path('fatura/', views.faturaTask, name='fatura-task'),
    path('helloworld/', views.helloworld),

]