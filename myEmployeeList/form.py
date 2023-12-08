from django.forms import ModelForm
from myEmployeeList.models import TeamMember
from django import forms

class TeamMemberForm(ModelForm):
  member_type = forms.ChoiceField(required = True, initial='regular', choices=TeamMember.CHOICES, widget=forms.RadioSelect())
  
  class Meta:
    model = TeamMember
    fields = '__all__'

