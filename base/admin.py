from django.contrib import admin
from . import models
from.models import ContactUs
from.models import BloodDonation


#--------------Patient Class--------------
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'id_num', 'disease', 'gender']
    list_filter = ['disease']
    list_display = ['first_name', 'last_name', 'age', 'address', 'id_num', 'disease', 'smoking', 'gender']
#--------------Doctor Class--------------
class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'id_num', 'specialization', 'experience', 'gender', 'doctor_of_the_month']
    list_filter = ['specialization', 'experience', 'doctor_of_the_month']
    list_display = ['first_name', 'last_name', 'age', 'id_num', 'educational_institution', 'specialization', 'experience', 'gender', 'doctor_of_the_month']
#--------------Appointment Class--------------
class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['patient_first_name', 'patient_last_name']
    list_filter = ['patient_first_name', 'patient_last_name']
    list_display = ['patient_first_name', 'patient_last_name', 'patient_email', 'patient_phone_number', 'appointment_date', 'appointment_time', 'description']
#--------------Admin Registers--------------
admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(ContactUs)
admin.site.register(BloodDonation)
admin.site.register(models.Appointment, AppointmentAdmin)
admin.site.register(models.Room)
admin.site.register(models.Message)

