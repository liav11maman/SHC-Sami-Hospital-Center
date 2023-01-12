from django.test import TestCase
from base.models import Patient, Doctor, Appointment


class TestModels(TestCase):


    def setUp(self):
        # Creating patient and doctor objects for the test
        self.patient1 = Patient.objects.create(
            first_name = 'first_name_patient1',
            last_name = 'last_name_patient1',
            age = 30,
            address = 'address_patient1',
            disease = 'disease_patient1',
            id_num = 123456789,
            smoking = 'N',
            gender = 'M',
        )
        self.doctor1 = Doctor.objects.create(
            first_name = 'first_name_doctor1',
            last_name = 'last_name_doctor1',
            age = 50,
            specialization = 'specialization_doctor1',
            educational_institution = 'educational_institution_doctor1',
            experience = 10,
            id_num = 123456789,
            gender = 'F',
        )
        self.appointment1 = Appointment.objects.create(
            patient_first_name = 'test',
            patient_last_name = 'test1',
            patient_email = 'test@test.com',
            patient_phone_number = '054-1234567',
            appointment_date = '2023-03-20',
            appointment_time = '12:30:00',
            description = 'test description'
        )
  
    
    def test_patient1_doctor1_first_name(self):
        # Test function to test the doctor and patient first name 
        self.assertTrue(self.patient1.first_name)
        self.assertTrue(self.doctor1.first_name)
        self.assertNotEqual(self.patient1.first_name, self.doctor1.first_name)


    def test_patient1_doctor1_last_name(self):
        # Test function to test the doctor and patient last name
        self.assertTrue(self.patient1.last_name)
        self.assertTrue(self.doctor1.last_name)
        self.assertNotEqual(self.patient1.last_name, self.doctor1.last_name)


    def test_patient1_doctor1_age(self):
        # Test function to test the doctor and patient age
        self.assertTrue(self.patient1.age)
        self.assertTrue(self.doctor1.age)
        self.assertNotEqual(self.patient1.age, self.doctor1.age)


    def test_patient1_address(self):
        # Test function to test the patient address
        self.assertTrue(self.patient1.address)


    def test_patient1_diesease(self):
        # Test function to test the patient diesease
        self.assertTrue(self.patient1.disease)


    def test_doctor1_specialization(self):
        # Test function to test the doctor specialization
        self.assertTrue(self.doctor1.specialization)


    def test_doctor1_educational_institution(self):
        # Test function to test the doctor educational institution
        self.assertTrue(self.doctor1.educational_institution)

    
    def test_doctor1_experience(self):
        # Test function to test the doctor experience
        self.assertTrue(self.doctor1.experience)


    def test_patient1_doctor1_id_num(self):
         # Test function to test the doctor and patient id numbers
        self.assertTrue(self.patient1.id_num)
        self.assertTrue(self.doctor1.id_num)
        self.assertEqual(self.patient1.id_num, self.doctor1.id_num)


    def test_patient1_smoking(self):
        # Test function to test the patient smoking
        self.assertTrue(self.patient1.smoking)


    def test_patient1_doctor1_gender(self):
        # Test function to test the doctor and patient gender
        self.assertTrue(self.patient1.gender)
        self.assertNotEqual(self.patient1.gender, self.doctor1.gender)

    def test_appointment_patient_name(self):
        self.assertTrue(self.appointment1.patient_first_name)
        