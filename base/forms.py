from django import forms
from .models import Patient
 
class EditPatientForm(forms.ModelForm):
 
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "age", "address", "disease", "id_num", "smoking", "gender"]