from django.db import models

# Create your models here.

class TeamMember(models.Model):
  first_name = models.CharField(max_length = 25, blank = False, null = False)
  last_name = models.CharField(max_length = 25, blank = False, null = False)
  email = models.EmailField(blank = False, null = False)
  phone_number = models.CharField(max_length = 25, blank = False, null = False)
  
  CHOICES = [
    ('regular', 'Regular'),
    ('admin', 'Admin'),
  ]
  member_type = models.CharField(max_length=10, choices=CHOICES)


  def __str__(self):
    return self.first_name + " " + self.last_name