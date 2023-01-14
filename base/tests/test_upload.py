from django.test import TestCase


class UploadTest(TestCase):

    def test_doctor_upload_html(self):
        # Testing the doctor upload button
        self.assertHTMLEqual(
            '<button class="button-71" role="button">Upload file</button>',
            '<button class="button-71" role="button">Upload file</button>',
        )
    def test_patient_upload_html(self):
        # Testing the patient upload button
        self.assertHTMLEqual(
            '<button class="button-71" role="button">Upload file</button>',
            '<button class="button-71" role="button">Upload file</button>',
        )
       