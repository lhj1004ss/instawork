from django.shortcuts import render, HttpResponse, redirect
# from django.views.decorators.csrf import csrf_exempt
from myEmployeeList.form import TeamMemberForm
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

  return render(request, "add.html", context)

def edit(request):
  return render(request, "edit.html")