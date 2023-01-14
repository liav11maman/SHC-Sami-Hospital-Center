from django.test import TestCase
from base.models import Patient, Doctor, Appointment, ContactUs, BloodDonation, Message, Room
from datetime import date,time, datetime


class TestModels(TestCase):


    def setUp(self):
        # Creating objects for the test
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
            appointment_date = date(2022,1,14),
            appointment_time = time(12,0),
            description = None
        )

        self.contact1 = ContactUs.objects.create(
            name = 'person',
            phone = '054-9856231',
            email = 'person@gmail.com',
            subject = 'somthing',
            message = None
        )

        self.blood_doner1 = BloodDonation.objects.create(
            first_name = 'David',
            last_name = 'Smith',
            email = 'david.com',
            address = 'new york',
            phone = None,
            blood_type = 'AB'
        )

        self.my_message = Message.objects.create(
            value = "my message",
            date = datetime(2022,4,16,12,30,00),
            user = "username",
            room = 'room name'
        )

        self.my_room = Room.objects.create(
            name = "my room"
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
        
    def test_appointment_patient_first_name(self):
        # Test function to test the appointment patient first name
        self.assertEqual(self.appointment1.patient_first_name, "test")

    def test_appointment_patient_last_name(self):
        # Test function to test the appointment patient last name
        self.assertEqual(self.appointment1.patient_last_name, "test1")

    def test_appointment_patient_email(self):
        # Test function to test the appointment patient email 
        self.assertIsNotNone(self.appointment1.patient_email)

    def test_appointment_patient_phone_number(self):
        # Test function to test the appointment patient phone number
       self.assertEqual(self.appointment1.patient_phone_number, "054-1234567")       

    def test_appointment_date(self):
        # Test function to test the appointment date
       self.assertTrue(isinstance(self.appointment1.appointment_date, date))      

    def test_appointment_time(self):
        # Test function to test the appointment time
       self.assertTrue(isinstance(self.appointment1.appointment_time, time))    

    def test_appointment_description(self):
        # Test function to test the appointment description
       self.assertIsNone(self.appointment1.description)

    def test_contact_name(self):
        # Test function to test the contact us name
        self.assertEqual(self.contact1.name, 'person')   

    def test_contact_phone(self):
        # Test function to test the contact us phone
        self.assertFalse(isinstance(self.contact1.phone, float))    

    def test_contact_email(self):
        # Test function to test the contact us email
        self.assertIn('@',self.contact1.email)  

    def test_contact_subject(self):
        # Test function to test the contact us subject
        self.assertIsNotNone(self.contact1.subject)    

    def test_contact_message(self):
        # Test function to test the contact us message
        self.assertIsNone(self.contact1.message)    

    def test_blood_doner_name(self):
        # Test function to test the blood donation name 
        self.assertEqual(self.blood_doner1.first_name, 'David')
        self.assertNotEqual(self.blood_doner1.last_name, 'Cohen')    

    def test_blood_doner_email(self):
        # Test function to test the blood donation email
        self.assertIn('@',self.contact1.email)  

    def test_blood_doner_phone(self):
        # Test function to test the blood donation phone
        self.assertIsNone(self.blood_doner1.phone)

    def test_blood_doner_type(self):
        # Test function to test the blood donation blood type
        types = ['A', 'A+', 'B', 'B+', 'AB', 'AB+', 'O', 'O+']
        self.assertIn(self.blood_doner1.blood_type, types)

    def test_message_value(self):
        # Test function to test the message
        msg = 'my message'
        self.assertIs(msg, self.my_message.value)

    def test_message_datetime(self):
        # Test function to test the message date and time
        self.assertTrue(isinstance(self.my_message.date, datetime))

    def test_message_room(self):
        # Test function to test the message
        self.assertIsNotNone(self.my_message.room)

    def test_room_name(self):
        # Test function to test the room
        self.assertTrue(isinstance(self.my_room.name, str))
