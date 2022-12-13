from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import home, signup, signin, signout, pharmacy, blood_donation

class TestUrls(SimpleTestCase):
    
    def test_home_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_signup_resolves(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_signin_resolves(self):
        url = reverse('signin')
        self.assertEquals(resolve(url).func, signin)

    def test_backhome_resolves(self):
        url = reverse('backhome')
        self.assertEquals(resolve(url).func, signout)

    def test_pharmacy_resolves(self):
        url = reverse('pharmacy')
        self.assertEquals(resolve(url).func, pharmacy)

    def test_blood_donation_resolves(self):
        url = reverse('blood_donation')
        self.assertEquals(resolve(url).func, blood_donation)



