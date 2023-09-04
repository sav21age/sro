from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from pages.models import IndexPage


class IndexPageTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test index detail view """

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_detail_not_exists(self):
        """ Test index detail view not exists """

        self.assertRaises(ObjectDoesNotExist, IndexPage.objects.get, id=1000000000)
