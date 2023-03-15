from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase

from upload_app.infrastructure.serializers import CSVUploadSerializer

class CSVUploadSerializerTestCase(APITestCase):

    def test_serializer_with_valid_data(self):
        csv_data = "column1,column2\nvalue1,value2"
        csv_file = SimpleUploadedFile("test.csv", csv_data.encode('utf-8'))
        data = {'file': csv_file}
        serializer = CSVUploadSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_data(self):
        data = {'file': 'not_a_file'}
        serializer = CSVUploadSerializer(data=data)

        self.assertFalse(serializer.is_valid())