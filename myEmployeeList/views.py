from curses.ascii import NUL
from django.shortcuts import render, redirect
from myEmployeeList.form import TeamMemberForm
from .models import TeamMember
from django.views import View

# Create your views here.

class TeamMemberList(View):
  def get(self, request):
    teamMemberData = TeamMember.objects.all()
    context = {"teamMemberData": teamMemberData}
    return render(request, "list.html", context)
    
class AddTeamMember(View):
  def get(self, request):
    teamMemberForm = TeamMemberForm
    context= {"teamMemberForm" : teamMemberForm }
    return render(request, "add.html", context)

  def post(self, request):
    form = TeamMemberForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')

class EditTeamMember(View):
  def get(self, request, pk):
    selectedTeamMember = TeamMember.objects.get(id = pk)
    selectedTeamMemberForm = TeamMemberForm(instance = selectedTeamMember) 
    context = {'selectedTeamMemberForm' : selectedTeamMemberForm, 
    'selectedTeamMemberId': pk}
    return render(request, "edit.html", context)

  def post(self, request, pk):
    selectedTeamMember = TeamMember.objects.get(id = pk)
    form = TeamMemberForm(request.POST, instance = selectedTeamMember)
    if form.is_valid():
      form.save()
      return redirect('/')

class DeleteTeamMember(View):
  def get(self, request, pk):
    selectedTeamMember = TeamMember.objects.get(id = pk)
    selectedTeamMember.delete()
    return redirect('/')