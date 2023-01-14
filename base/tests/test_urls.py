from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import send, checkview, live_chat_home, confirm_appointment, appointment, doctor_of_the_month, doctor_upload, home, signup, signin, signout, pharmacy, blood_donation, signup2, signin2, patient_panel, aboutus, patient_upload, medical_info, cardiology, pediatrics, maternity_department, kidney_transplant, neurology, cancer_medicine, urology_department, ophthalmology, orthopedics, thanks, doctor_panel, show_patients_information


class TestUrls(SimpleTestCase):
    # -------------Test-Home urls--------------
    def test_home_resolves(self):
        # Testing the home url
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    # -------------Test-Login and Logout urls--------------

    def test_signup_resolves(self):
        # Testing the signup url
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_signin_resolves(self):
        # Testing the signin url
        url = reverse('signin')
        self.assertEquals(resolve(url).func, signin)

    def test_signout_resolves(self):
        # Testing the backhome url
        url = reverse('signout')
        self.assertEquals(resolve(url).func, signout)

    def test_signup2_resolves(self):
        # Testing the signup2 url
        url = reverse('signup2')
        self.assertEquals(resolve(url).func, signup2)

    def test_signin2_resolves(self):
        # Testing the signin2 url
        url = reverse('signin2')
        self.assertEquals(resolve(url).func, signin2)
    # -------------Test-Patient urls--------------

    def test_patient_resolves(self):
        # Testing the paitent url
        url = reverse('patient_panel')
        self.assertEquals(resolve(url).func, patient_panel)

    def test_pharmacy_resolves(self):
        # Testing the pharmacy url
        url = reverse('pharmacy')
        self.assertEquals(resolve(url).func, pharmacy)

    def test_blood_donation_resolves(self):
        # Testing the blood donations url
        url = reverse('blood_donation')
        self.assertEquals(resolve(url).func, blood_donation)

    def test_aboutus_resolves(self):
        # Testing the aboutus url
        url = reverse('aboutus')
        self.assertEquals(resolve(url).func, aboutus)

    def test_patient_upload_resolves(self):
        # Testing the patient_upload url
        url = reverse('patient_upload')
        self.assertEquals(resolve(url).func, patient_upload)

    def test_doctor_upload_resolves(self):
        # Testing the patient_upload url
        url = reverse('doctor_upload')
        self.assertEquals(resolve(url).func, doctor_upload)

    def test_medical_info_resolves(self):
        # Testing the medical_info url
        url = reverse('medical_info')
        self.assertEquals(resolve(url).func, medical_info)

    def test_cardiology_resolves(self):
        # Testing the cardiology url
        url = reverse('cardiology')
        self.assertEquals(resolve(url).func, cardiology)

    def test_pediatrics_resolves(self):
        # Testing the pediatrics url
        url = reverse('pediatrics')
        self.assertEquals(resolve(url).func, pediatrics)

    def test_maternity_department_resolves(self):
        # Testing the maternity_department url
        url = reverse('maternity_department')
        self.assertEquals(resolve(url).func, maternity_department)

    def test_kidney_transplant_resolves(self):
        # Testing the kidney_transplant url
        url = reverse('kidney_transplant')
        self.assertEquals(resolve(url).func, kidney_transplant)

    def test_neurology_resolves(self):
        # Testing the neurology url
        url = reverse('neurology')
        self.assertEquals(resolve(url).func, neurology)

    def test_cancer_medicine_resolves(self):
        # Testing the cancer_medicine url
        url = reverse('cancer_medicine')
        self.assertEquals(resolve(url).func, cancer_medicine)

    def test_urology_department_resolves(self):
        # Testing the urology_department url
        url = reverse('urology_department')
        self.assertEquals(resolve(url).func, urology_department)

    def test_ophthalmology_resolves(self):
        # Testing the ophthalmology url
        url = reverse('ophthalmology')
        self.assertEquals(resolve(url).func, ophthalmology)

    def test_orthopedics_resolves(self):
        # Testing the orthopedics url
        url = reverse('orthopedics')
        self.assertEquals(resolve(url).func, orthopedics)

    def test_thanks_resolves(self):
        # Testing the thanks url
        url = reverse('thanks')
        self.assertEquals(resolve(url).func, thanks)
# -------------Test-Doctor urls--------------

    def test_doctor_panel_resolves(self):
        # Testing the doctor_panel url
        url = reverse('doctor_panel')
        self.assertEquals(resolve(url).func, doctor_panel)

    def test_patients_information_resolves(self):
        # Testing the patients_information url
        url = reverse('doctor_pat_info')
        self.assertEquals(resolve(url).func, show_patients_information)

    def test_doctor_of_the_month_resolves(self):
        # Testing the doctor_of_the_month url
        url = reverse('doctor_of_the_month')
        self.assertEquals(resolve(url).func, doctor_of_the_month)
# -------------Test-Appointment urls--------------

    def test_appointment_resolves(self):
        # Testing the appointment url
        url = reverse('appointment')
        self.assertEquals(resolve(url).func, appointment)

    def test_confirm_appointment_resolves(self):
        # Testing the confirm_appointment url
        url = reverse('confirm_appointment')
        self.assertEquals(resolve(url).func, confirm_appointment)
    # ----------Test-Live Chat urls-----------------

    def test_live_chat_home_resolves(self):
        # Testing the live_chat_home url
        url = reverse('live_chat_home')
        self.assertEquals(resolve(url).func, live_chat_home)


    def test_live_chat_home_checkview_resolves(self):
        # Testing the live_chat_home/checkview url
        url = reverse('checkview')
        self.assertEquals(resolve(url).func, checkview)

    def test_send_resolves(self):
        # Testing the send url
        url = reverse('send')
        self.assertEquals(resolve(url).func, send)
