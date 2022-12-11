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


admin.site.register(models.Patient, PatientAdmin)
<<<<<<< HEAD
admin.site.register(models.Doctor, DoctorAdmin)



=======
admin.site.register(models.Doctor, DoctorAdmin)
>>>>>>> GuyEzra
