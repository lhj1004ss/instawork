from django.urls import path, include
from myEmployeeList import views

urlpatterns = [
  path('', views.index),
  path('add/', views.addTeamMember),
  path('edit/<id>/', views.editTeamMember)
]
