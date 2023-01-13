from django.test import TestCase, Client
from django.urls import reverse
from base.models import Patient, Doctor
import json


class TestViews(TestCase):

    def setup(self):
        self.client = Client()
# --------------Home test--------------

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
# --------------patients_informations test--------------
    # def test_patients_information(self):
    #     response=self.client.get(reverse('doctor_pat_info'))
    #     self.assertTemplateUsed(response,'patients_information.html')
# --------------pharmacy test--------------

    def test_pharmacy(self):
        response = self.client.get(reverse('pharmacy'))
        self.assertTemplateUsed(response, 'pharmacy.html')
# --------------patient_panel test--------------

    # def test_patient_panel(self):
    #     response = self.client.get(reverse('patient_panel'))
    #     self.assertTemplateUsed(response, 'patient_panel.html')
# --------------doctor_panel test--------------
    # def test_doctor_panel(self):
    #     response = self.client.get(reverse('doctor_panel'))
    #     self.assertTemplateUsed(response, 'doctor_panel.html')
# --------------blood_donation test--------------

    def test_blood_donation(self):
        response = self.client.get(reverse('blood_donation'))
        self.assertTemplateUsed(response, 'blood_donation.html')
# --------------aboutus test--------------

    def test_aboutus(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'aboutus.html')
# --------------doctor_upload test--------------

    def test_doctor_upload(self):
        response = self.client.get(reverse('doctor_upload'))
        self.assertTemplateUsed(response, 'doctor_upload.html')
# --------------patient_upload test--------------

    def test_patient_upload(self):
        response = self.client.get(reverse('patient_upload'))
        self.assertTemplateUsed(response, 'patient_upload.html')
# --------------doctor_of_the_month test--------------

    def test_doctor_of_the_month(self):
        response = self.client.get(reverse('doctor_of_the_month'))
        self.assertTemplateUsed(response, 'doctor_of_the_month.html')
# --------------medical_info test--------------

    def test_medical_info(self):
        response = self.client.get(reverse('medical_info'))
        self.assertTemplateUsed(response, 'medical_info.html')


# --------------signin test--------------

    def test_signin(self):
        response = self.client.get(reverse('signin'))
        self.assertTemplateUsed(response, 'signin.html')
# --------------signup test--------------

    def test_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')
