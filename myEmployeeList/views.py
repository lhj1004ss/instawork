from django.shortcuts import render, HttpResponse, redirect
# from django.views.decorators.csrf import csrf_exempt
from myEmployeeList.template.form import TeamMemberForm

# Create your views here.
# teamMembers = [
#   {'id': 1, 'firstName': 'Adrien', 'lastName': 'Olczck', 'email': 'adrien@instawork.com', 'phone':'415-310-1619', 'admin': True },
#   {'id': 2, 'firstName': 'Charlene', 'lastName': 'Pham', 'email': 'charlene@instawork.com', 'phone':'415-310-1619', 'admin': False },
#   {'id': 3, 'firstName': 'Benson', 'lastName': 'Mach', 'email': 'benson@instawork.com', 'phone':'415-310-1619', 'admin': False },
#   {'id': 4, 'firstName': 'Den', 'lastName': 'Petrie', 'email': 'den@instawork.com', 'phone':'415-310-1619', 'admin': False },
#   ]


def index(request):
  form = TeamMemberForm
  context = {'form': form}
  return render(request, "index.html", context)

def add(request):
  return render(request, "add.html")

def edit(request):
  return render(request, "edit.html")