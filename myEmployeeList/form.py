from django.forms import ModelForm
from myEmployeeList.models import TeamMember
from django import forms

class TeamMemberForm(ModelForm):
  class Meta:
    model = TeamMember
    fields = '__all__'

class RoleForm(forms.Form):
    regular = 'regular'
    admin = 'admin'

    CHOICES = [
        (regular, 'regular'),
        (admin, 'admin'),
    ]

    checkbox_field = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

