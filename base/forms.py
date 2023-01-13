from django import forms
from .models import Patient, Appointment

 #--------------Edit Patient Form-------------- 
class EditPatientForm(forms.ModelForm):
 
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "age", "address", "disease", "id_num", "smoking", "gender"]


class EditPatientAppointment(forms.ModelForm):
 
    class Meta:
        model = Appointment
        fields = ["patient_first_name", "patient_last_name", "patient_email", "patient_phone_number", "appointment_date", "appointment_time"]