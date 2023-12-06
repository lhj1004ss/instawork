from django.forms import ModelForm
from myEmployeeList.models import TeamMember

class TeamMemberForm(ModelForm):
  class Meta:
    model = TeamMember
    fields = '__all__'