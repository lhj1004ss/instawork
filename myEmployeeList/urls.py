from django.urls import path, include
from myEmployeeList import views

urlpatterns = [
  path('', views.index, name='index'),  
  path('add/', views.add, name='add'),
  path('edit/<id>/', views.edit, name='edit'),
]

