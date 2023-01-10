from django.contrib import admin
from . import models
from.models import ContactUs
from.models import BloodDon

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'id_num', 'disease', 'gender']
    list_filter = ['disease']
    list_display = ['first_name', 'last_name', 'age', 'address', 'id_num', 'disease', 'smoking', 'gender']

class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'id_num', 'specialization', 'experience', 'gender', 'doctor_of_the_month']
    list_filter = ['specialization', 'experience', 'doctor_of_the_month']
    list_display = ['first_name', 'last_name', 'age', 'id_num', 'educational_institution', 'specialization', 'experience', 'gender', 'doctor_of_the_month']


admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(ContactUs)
admin.site.register(BloodDon)

