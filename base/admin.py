from django.contrib import admin
from . import models


# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'id_num', 'disease', 'gender']
    list_filter = ['disease']
    list_display = ['first_name', 'last_name', 'age', 'address', 'id_num', 'disease', 'smoking', 'gender']

class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'id_num', 'specialization', 'experience', 'gender']
    list_filter = ['specialization', 'experience']
    list_display = ['first_name', 'last_name', 'age', 'id_num', 'educational_institution', 'specialization', 'experience', 'gender']

class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['patient_first_name', 'patient_last_name']
    list_filter = ['patient_first_name', 'patient_last_name']
    list_display = ['patient_first_name', 'patient_last_name', 'patient_email', 'patient_phone_number', 'appointment_date', 'appointment_time', 'description']



admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Appointment, AppointmentAdmin)
admin.site.register(models.Room)
admin.site.register(models.Message)
admin.site.register(models.ContactUs)
admin.site.register(models.BloodDonation)


