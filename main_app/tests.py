from django.test import TestCase
from .models import DataRecord

class DataRecordTestCase(TestCase):
    def test_create_record(self):
        rec = DataRecord.objects.create(name="Test", info="Testing")
        self.assertEqual(str(rec), "DataRecord(Test)")
