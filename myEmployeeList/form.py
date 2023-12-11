from django.forms import ModelForm
from myEmployeeList.models import TeamMember
from django import forms

class TeamMemberForm(ModelForm):
  member_type = forms.ChoiceField(required = True, initial='regular', choices=TeamMember.CHOICES, widget=forms.RadioSelect())
  
  class Meta:
    model = TeamMember
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(TeamMemberForm, self).__init__(*args, **kwargs)

    placeholders = {
        'first_name': 'Enter first name',
        'last_name': 'Enter last name',
        'email': 'Enter email',
        'phone_number': 'Enter phone number',
    }
    for field_name, placeholder in placeholders.items():
        self.fields[field_name].widget.attrs['placeholder'] = placeholder


