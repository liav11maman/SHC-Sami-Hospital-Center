from django.test import TestCase


class PatientsInformationTest(TestCase):

    def test_patients_information_html(self):
        # Testing the html table values
        self.assertHTMLEqual(
            '<td scope="col">First Name</td>',
            '<td scope="col">First Name</td>',
        )
        self.assertHTMLEqual(
            '<td scope="col">Age</td>',
            '<td scope="col">Age</td>',
        )
        self.assertHTMLEqual(
            '<td scope="col">Address</td>',
            '<td scope="col">Address</td>',
        )
        self.assertHTMLEqual(
            '<td scope="col">Disease</td>',
            '<td scope="col">Disease</td>',
        )
        self.assertHTMLEqual(
            '<td scope="col">ID Number</td>',
            '<td scope="col">ID Number</td>',
        )
        self.assertHTMLEqual(
            '<td scope="col">Smoking</td>',
            '<td scope="col">Smoking</td>',
        )
        self.assertHTMLEqual(
            '<td scope="col">Gender</td>',
            '<td scope="col">Gender</td>',
        )
        
        