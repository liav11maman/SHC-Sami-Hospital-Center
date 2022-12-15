from django.test import TestCase
from base.models import Patient, Doctor


class TestModels(TestCase):


    def setUp(self):
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
  
    
    def test_patient1_doctor1_first_name(self):
        self.assertTrue(self.patient1.first_name)
        self.assertTrue(self.doctor1.first_name)
        self.assertNotEqual(self.patient1.first_name, self.doctor1.first_name)


    def test_patient1_doctor1_last_name(self):
        self.assertTrue(self.patient1.last_name)
        self.assertTrue(self.doctor1.last_name)
        self.assertNotEqual(self.patient1.last_name, self.doctor1.last_name)


    def test_patient1_doctor1_age(self):
        self.assertTrue(self.patient1.age)
        self.assertTrue(self.doctor1.age)
        self.assertNotEqual(self.patient1.age, self.doctor1.age)


    def test_patient1_address(self):
        self.assertTrue(self.patient1.address)


    def test_patient1_diesease(self):
        self.assertTrue(self.patient1.disease)


    def test_doctor1_specialization(self):
        self.assertTrue(self.doctor1.specialization)


    def test_doctor1_educational_institution(self):
        self.assertTrue(self.doctor1.educational_institution)

    
    def test_doctor1_experience(self):
        self.assertTrue(self.doctor1.experience)


    def test_patient1_doctor1_id_num(self):
        self.assertTrue(self.patient1.id_num)
        self.assertTrue(self.doctor1.id_num)
        self.assertEqual(self.patient1.id_num, self.doctor1.id_num)


    def test_patient1_smoking(self):
        self.assertTrue(self.patient1.smoking)


    def test_patient1_doctor1_gender(self):
        self.assertTrue(self.patient1.gender)
        self.assertNotEqual(self.patient1.gender, self.doctor1.gender)