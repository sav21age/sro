#https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
from datetime import datetime
from django.test import TestCase
from documents.models import DecisionMeeting, Inspection, TechnicalRegulation
from django.core.files.uploadedfile import SimpleUploadedFile
import shutil
import tempfile
from django.test import TestCase, override_settings


MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class DocumentTest(TestCase):
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)  # delete the temp dir
        super().tearDownClass()

    def test_document_name(self):
        """ Test document with name """
        doc = TechnicalRegulation()
        doc.name = 'Очень длинное название документа с именем'
        doc.file_path = SimpleUploadedFile(
            'Очень длинное название документа с именем.zip',
            b'-'
        )
        doc.upload_to = '/temp/'
        doc.save()
        self.assertEqual(doc.file_path, 'files/temp/Ochen_dlinnoe_nazvanie_dokumenta_s_imenem.zip')
        self.assertEqual(doc.__str__(), 'Очень длинное название документа с именем')


    def test_document_year(self):
        """ Test document with year """
        doc = Inspection()
        doc.year = '2000'
        doc.file_path = SimpleUploadedFile(
            'Очень длинное название документа с годом.zip',
            b'-'
        )
        doc.upload_to = '/temp/'
        doc.save()
        self.assertEqual(doc.file_path, 'files/temp/Ochen_dlinnoe_nazvanie_dokumenta_s_godom.zip')
        self.assertEqual(doc.__str__(), '2000')


    def test_document_date(self):
        """ Test document with date """
        doc = DecisionMeeting()
        doc.date = datetime.strptime('01-01-2023', "%d-%m-%Y").date()
        doc.name = 'Очень длинное название документа с датой'
        doc.file_path = SimpleUploadedFile(
            'Очень длинное название документа с датой.zip',
            b'-'
        )
        doc.upload_to = '/temp/'
        doc.save()
        self.assertEqual(doc.file_path, 'files/temp/2023-01-01_Ochen_dlinnoe_nazvanie_dokumenta_s_datoj.zip')
        self.assertEqual(doc.__str__(), f'{doc.name} от {doc.date.strftime("%d.%m.%Y")} г.')
