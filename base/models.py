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

class Appointment(models.Model):
    dte = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    time = models.TimeField()
    address = models.CharField(max_length=64)
    symptoms = models.TextField(blank=True)

    def __str__(self):
        return self.dte + ' ' + self.time

    class Meta:
        ordering = ["-dte"]

    

# class Appointments(models.Model):

#     patientId = models.BigIntegerField()
#     doctorId = models.BigIntegerField()
#     patientName = models.CharField(max_length=40,null=True)
#     doctorName = models.CharField(max_length=40,null=True)
#     appointmentDate = models.DateField(auto_now=True)
#     description = models.TextField(null=True, blank=True, max_length=500)
#     status = models.BooleanField(default=False)

