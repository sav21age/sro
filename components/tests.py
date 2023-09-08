#https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
from datetime import date
from django.core.exceptions import ValidationError
from django.test import TestCase
from components.models import Location, Member, News, OrgForm, Position
from django.core.files.uploadedfile import SimpleUploadedFile
import shutil
import tempfile
from django.test import TestCase, override_settings
from django.contrib.contenttypes.models import ContentType
from files.models import File


MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class NewsTest(TestCase):
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)  # delete the temp dir
        super().tearDownClass()

    def test_news(self):
        """ Test news """
        obj = News()
        obj.date = '2023-01-01'
        obj.description = 'Свежая новость'
        obj.save()

        file = File.objects.create(
            object_id = obj.id,
            content_type_id = ContentType.objects.get_for_model(obj).id,
            name = 'Очень длинное название новости',
            path = SimpleUploadedFile(
                'Очень длинное название новости.zip',
                b'-'
            ),
        )
        obj.files.set([file,])
        obj.save()

        for file in obj.files.all():
            self.assertEqual(file.path, 'files/Ochen_dlinnoe_nazvanie_novosti.zip')
        
        self.assertEqual(obj.__str__(), '2023-01-01')


class MemberTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.reg_num = 'СРО ПБ-170-999-2022'
        self.reg_date = date.today()
        self.inn = '9999999999'
        self.ogrn = '9999999999999'
        self.location = Location.objects.order_by('id').first()
        self.org_form = OrgForm.objects.order_by('id').first()
        self.company_fullname = '"Производственная компания "ПК"'
        self.company_shortname = '"ПК"'
        self.position = Position.objects.order_by('id').first()
        self.lastname = 'Иванов'
        self.firstname = 'Иван'
        self.patronymic = 'Иванович'
        self.excluded = True
        self.excluded_date = '2023-01-01'


    def test_ok(self):
        """ Test ok """

        obj = Member()
        obj.reg_num = self.reg_num
        obj.reg_date = self.reg_date
        obj.inn = self.inn
        obj.ogrn = self.ogrn
        obj.location = self.location
        obj.org_form = self.org_form
        obj.company_fullname = self.company_fullname
        obj.company_shortname = self.company_shortname
        obj.position = self.position
        obj.lastname = self.lastname
        obj.firstname = self.firstname
        obj.patronymic = self.patronymic
        obj.full_clean()
        obj.save()
        
        self.assertEqual(obj.__str__(), 'ИП «Производственная компания «ПК»')
        self.assertEqual(obj.reg_num, self.reg_num)
        self.assertEqual(obj.get_company_fullname, 'ИП «Производственная компания «ПК»')
        self.assertEqual(obj.get_company_shortname, 'ИП «ПК»')


    def test_excluded(self):
        """ Test excluded """

        obj = Member()
        obj.reg_num = self.reg_num
        obj.reg_date = self.reg_date
        obj.inn = self.inn
        obj.ogrn = self.ogrn
        obj.location = self.location
        obj.org_form = self.org_form
        obj.company_fullname = self.company_fullname
        obj.company_shortname = self.company_shortname
        obj.position = self.position
        obj.lastname = self.lastname
        obj.firstname = self.firstname
        obj.patronymic = self.patronymic
        obj.excluded = self.excluded

        self.assertRaises(ValidationError, obj.full_clean, {'excluded_date': ['Обязательное поле.']})
    

    def test_excluded_date(self):
        """ Test excluded date """

        obj = Member()
        obj.reg_num = self.reg_num
        obj.reg_date = self.reg_date
        obj.inn = self.inn
        obj.ogrn = self.ogrn
        obj.location = self.location
        obj.org_form = self.org_form
        obj.company_fullname = self.company_fullname
        obj.company_shortname = self.company_shortname
        obj.position = self.position
        obj.lastname = self.lastname
        obj.firstname = self.firstname
        obj.patronymic = self.patronymic
        obj.excluded_date = self.excluded_date

        self.assertRaises(ValidationError, obj.full_clean, {'excluded': ['Обязательное поле.']})


    def test_shortname(self):
        """ Test shortname """

        obj = Member()
        obj.reg_num = self.reg_num
        obj.reg_date = self.reg_date
        obj.inn = self.inn
        obj.ogrn = self.ogrn
        obj.location = self.location
        obj.org_form = self.org_form
        obj.company_fullname = self.company_fullname
        obj.position = self.position
        obj.lastname = self.lastname
        obj.firstname = self.firstname
        obj.patronymic = self.patronymic

        self.assertRaises(ValidationError, obj.full_clean, {'company_shortname': ['Обязательное поле.']})


    def test_fullname(self):
        """ Test fullname """

        obj = Member()
        obj.reg_num = self.reg_num
        obj.reg_date = self.reg_date
        obj.inn = self.inn
        obj.ogrn = self.ogrn
        obj.location = self.location
        obj.org_form = self.org_form
        obj.company_shortname = self.company_shortname
        obj.position = self.position
        obj.lastname = self.lastname
        obj.firstname = self.firstname
        obj.patronymic = self.patronymic

        self.assertRaises(ValidationError, obj.full_clean, {'company_fullname': ['Обязательное поле.']})
