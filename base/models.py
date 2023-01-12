from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime
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

    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    age = models.PositiveIntegerField(null=True)
    specialization = models.CharField(max_length=64, null=True)
    educational_institution = models.CharField(max_length=64, null=True)
    experience = models.PositiveIntegerField(null=True)
    id_num = models.BigIntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Appointment(models.Model):

    patient_first_name = models.CharField(max_length=50, null=True)
    patient_last_name = models.CharField(max_length=50, null=True)
    patient_email = models.EmailField(max_length=50, null=True)
    patient_phone_number = models.CharField(max_length=50, null=True)
    appointment_date = models.DateField(auto_now_add=False, null=True, blank=True)
    appointment_time = models.TimeField(auto_now_add=False, null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return self.patient_first_name + ' ' + self.patient_last_name
    
#------------live chat------------------

class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return 'Room name: ' + self.name


    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    def __str__(self):
        return 'from user: ' + self.user


 #--------------Contact Us Model-------------- 
class ContactUs(models.Model):

    name=models.CharField(max_length=40,null=True)
    phone=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=40,null=True)
    subject=models.CharField(max_length=40,null=True)
    message=models.TextField(max_length=40,null=True)

    def __str__(self):
        return self.name

 #--------------Blood Donations Model-------------- 
class BloodDonation(models.Model):
        
    first_name=models.CharField(max_length=40,null=True)
    last_name=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=40,null=True)
    address=models.TextField(max_length=40,null=True)
    phone=models.CharField(max_length=40,null=True)
    blood_type=models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.first_name