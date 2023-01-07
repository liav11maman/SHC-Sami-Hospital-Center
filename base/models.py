from django.db import models
from django.contrib.auth.models import User


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
    DOCTOR_OF_THE_MONTH_CHOICE = (('Y', 'Yes'), ('N', 'No'))

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    specialization = models.CharField(max_length=64)
    educational_institution = models.CharField(max_length=64)
    experience = models.PositiveIntegerField()
    id_num = models.BigIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    doctor_of_the_month = models.CharField(max_length=1, choices=DOCTOR_OF_THE_MONTH_CHOICE)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


