from django.db import models
from django import forms

# Create your models here.

class TeamMember(models.Model):
  first_name = models.CharField(max_length=25, blank=False, null= False)
  last_name = models.CharField(max_length=25, blank=False, null= False)
  email = models.EmailField(blank=False, null= False)
  phone_number = models.IntegerField(blank=False, null= False)

  def __str__(self):
    return self.first_name + self.last_name + self.email + self.phone_number
