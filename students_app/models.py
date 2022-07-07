from django.db import models

# Create your wonderful models here.
class Student(models.Model):
    first_name = models.CharField("First name", max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    date_of_birth = models.DateField("Date of birth")
    phone_number = models.CharField("Phone number", max_length=30)
    email = models.EmailField("Email")



def save(self, *args, **kwargs):
    self.first_name = self.first_name.capitalize()
    self.last_name = self.last_name.capitalize()
