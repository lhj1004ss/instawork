from django.urls import path, include
from myEmployeeList import views

urlpatterns = [
  path('', views.TeamMemberList.as_view(), name ='list'),  
  path('add/', views.AddTeamMember.as_view(), name ='add'),
  path('edit/<str:pk>/', views.EditTeamMember.as_view(), name = 'edit'),
  path('delete/<str:pk>/', views.DeleteTeamMember.as_view(), name = "delete")
]

