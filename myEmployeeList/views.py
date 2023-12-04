from django.shortcuts import render, HttpResponse

# Create your views here.
teamMembers = [
  {'id': 1, 'firstName': 'Adrien', 'lastName': 'Olczck', 'email': 'adrien@instawork.com', 'phone':'415-310-1619', 'admin': True },
  {'id': 2, 'firstName': 'Charlene', 'lastName': 'Pham', 'email': 'charlene@instawork.com', 'phone':'415-310-1619', 'admin': False },
  {'id': 3, 'firstName': 'Benson', 'lastName': 'Mach', 'email': 'benson@instawork.com', 'phone':'415-310-1619', 'admin': False },
  {'id': 4, 'firstName': 'Den', 'lastName': 'Petrie', 'email': 'den@instawork.com', 'phone':'415-310-1619', 'admin': False },
  ]

def headerHTMLTemplate(title, description):
  return f'''
    <h2>{title}</h2>
    <p>{description}</p>
  '''
def memberInfoHTMLTemplate():
  return f'''
    <html>
      <body>
        <h3>Info</h3>
        <input/>
        </br>
        <input/>
        </br>
        <input/>
        </br>
        <input/>
        <h3>Role</h3>
      </body>
    </html>
  '''
def memberListHTMLTemplate():
  global teamMembers
  teamMember = ''
  for member in teamMembers:
    teamMember += f'''<a href="/edit/{member["id"]}"><div>{member["firstName"]} {member["lastName"]}</div></div>'''

  return f'''
    <html>
      <body>
          <a href="/add">+</a>
          {headerHTMLTemplate('Team Members', f'you have {len(teamMembers)} team members')}
          {teamMember}
      </body>
    </html>
  '''

def index(request):
  return HttpResponse(memberListHTMLTemplate())

def addTeamMember(request):
  return HttpResponse('add!')

def editTeamMember(request, id):
  return HttpResponse(memberInfoHTMLTemplate() + id)