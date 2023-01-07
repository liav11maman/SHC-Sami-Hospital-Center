from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    SMOKE_CHOICES = (('Y', 'Yes'), ('N', 'No'),)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=64)
    disease = models.CharField(max_length=64)
    id_num = models.BigIntegerField()
    smoking = models.CharField(max_length=1, choices=SMOKE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Doctor(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    specialization = models.CharField(max_length=64)
    educational_institution = models.CharField(max_length=64)
    experience = models.PositiveIntegerField()
    id_num = models.BigIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name




class ContactUs(models.Model):

    name=models.CharField(max_length=40,null=True)
    phone=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=40,null=True)
    subject=models.CharField(max_length=40,null=True)
    message=models.TextField(max_length=40,null=True)

    def __str__(self):
        return self.name


class BloodDon(models.Model):
        
    first_name=models.CharField(max_length=40,null=True)
    last_name=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=40,null=True)
    address=models.TextField(max_length=40,null=True)
    phone=models.CharField(max_length=40,null=True)
    blood_type=models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.first_name