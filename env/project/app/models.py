from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=50)
    desig = models.CharField(max_length=100)
    salary = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Signup(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Admission(models.Model):
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    RADIO_CHOICE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    preffered_subject = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_name