from django.db import models

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    SMOKE_CHOICES = (('Y', 'Yes'), ('N', 'No'),)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    disease = models.CharField(max_length=64)
    id_num = models.PositiveIntegerField()
    smoking = models.CharField(max_length=1, choices=SMOKE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class Doctor(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    specialization = models.CharField(max_length=64)
    educational_institution = models.CharField(max_length=64)
    experience = models.PositiveIntegerField()
    id_num = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)