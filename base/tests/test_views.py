from django.test import TestCase, Client
from django.urls import reverse
from base.models import Patient, Doctor
import json

class TestViews(TestCase):

    def setup(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_signin(self):
        response = self.client.get(reverse('signin'))
        self.assertTemplateUsed(response, 'signin.html')

    def test_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_pharmacy(self):
        response = self.client.get(reverse('pharmacy'))
        self.assertTemplateUsed(response, 'pharmacy.html')

    def test_blood_donation(self):
        response = self.client.get(reverse('blood_donation'))
        self.assertTemplateUsed(response, 'blood_donation.html')

    def test_aboutus(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'aboutus.html')

 

    
    