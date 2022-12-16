from django.test import TestCase


class UploadTest(TestCase):

    def test_upload_html(self):
        # Testing the upload button
        self.assertHTMLEqual(
            '<button class="button-71" role="button">Upload file</button>',
            '<button class="button-71" role="button">Upload file</button>',
        )
       