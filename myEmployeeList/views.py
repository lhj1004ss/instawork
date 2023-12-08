from django.shortcuts import render, redirect
from myEmployeeList.form import TeamMemberForm
from myEmployeeList.form import RoleForm

from .models import TeamMember

# Create your views here.

def index(request):
  teamMemberData = TeamMember.objects.all()
  context = {"teamMemberData": teamMemberData}
  return render(request, "index.html", context)

def add(request):
  form = TeamMemberForm
  context = {'form': form}
  if request.method == "POST":
    form = TeamMemberForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  elif request.method == "GET":
 

    return render(request, "add.html", context)

def edit(request, id):

  if request.method == "GET":
    selectedTeamMemberData = TeamMember.objects.get(id = id)
    form = TeamMemberForm(instance = selectedTeamMemberData)
    context = {'form' : form}
    if selectedTeamMemberData.regular == True:
      selectedTeamMemberData.admin == False
      print(selectedTeamMemberData.regular)
    else:
      print(selectedTeamMemberData.admin)
      selectedTeamMemberData.admin == True

    return render(request, "edit.html", context)
  


  elif request.method == "POST":
    selectedTeamMemberData = TeamMember.objects.get(id = id)
    
    return redirect('/')

