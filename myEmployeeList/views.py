from django.shortcuts import render, redirect
from myEmployeeList.form import TeamMemberForm
from .models import TeamMember

# Create your views here.

def index(request):
  teamMemberData = TeamMember.objects.all()
  context = {"teamMemberData": teamMemberData}
  return render(request, "index.html", context)

def add(request):
  teamMemberForm = TeamMemberForm
  if request.method == "POST":
    form = TeamMemberForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')


  return render(request, "add.html", {"teamMemberForm" : teamMemberForm })

def edit(request, id):
  if request.method == "GET":
    selectedTeamMemberData = TeamMember.objects.get(id = id)
    selectedTeamMemberForm = TeamMemberForm(instance = selectedTeamMemberData) 
    
    return render(request, "edit.html", {'selectedTeamMemberForm' : selectedTeamMemberForm })
  elif request.method == "POST":
    member = TeamMember.objects.get(pk=id)
    form = TeamMemberForm(request.POST, instance = member)
    if form.is_valid():
      form.save()
      return redirect('/')

