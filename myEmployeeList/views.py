from django.shortcuts import render, HttpResponse, redirect
# from django.views.decorators.csrf import csrf_exempt
from myEmployeeList.form import TeamMemberForm

# Create your views here.
# teamMembers = [
#   {'id': 1, 'firstName': 'Adrien', 'lastName': 'Olczck', 'email': 'adrien@instawork.com', 'phone':'415-310-1619', 'admin': True },
#   {'id': 2, 'firstName': 'Charlene', 'lastName': 'Pham', 'email': 'charlene@instawork.com', 'phone':'415-310-1619', 'admin': False },
#   {'id': 3, 'firstName': 'Benson', 'lastName': 'Mach', 'email': 'benson@instawork.com', 'phone':'415-310-1619', 'admin': False },
#   {'id': 4, 'firstName': 'Den', 'lastName': 'Petrie', 'email': 'den@instawork.com', 'phone':'415-310-1619', 'admin': False },
#   ]


def index(request):
  return render(request, "index.html",)

def add(request):
  form = TeamMemberForm
  context = {'form': form}

  if request.method == "POST":
    # print('request', request)
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    some_field = request.POST.get('some_field')
    print(first_name, last_name, email, phone_number, some_field)
    
  return render(request, "add.html", context)

def addTeamMember(request):
  if request.method == "POST":
    # print('request', request)
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    print(first_name, last_name, email, phone_number)

  return render(request, "index.html",)



def edit(request):
  return render(request, "edit.html")