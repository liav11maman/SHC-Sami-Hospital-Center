from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from base.models import Patient, Doctor


class MyTest(TestCase):
    client_class = Doctor

    def test_it(self):
        file = SimpleUploadedFile("file.txt", b"abc", content_type="text/plain")
        payload = {"file": file}
        response = self.client.post("/some/api/path/", payload, format="multipart")
        self.assertEqual(response.status_code, 201)

        # If you do more calls in this method with the same file then seek to zero
        file.seek(0)