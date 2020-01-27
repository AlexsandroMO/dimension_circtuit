

from django.urls import path
from . import views


urlpatterns = [
    path('homecalc', views.homecalc, name='home-calc'),
    path('newCalc/', views.newCalc, name='new-calc'),
    #path('newCalcResult/<int:id>', views.newCalcResult, name='new-calc-result'),
    #path('edittask/<int:id>', views.editTask, name='edit-task'),
    #path('deletetask/<int:id>', views.deleteTask, name='delete-task'),


]
