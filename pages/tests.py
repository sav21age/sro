from django.test import TestCase, Client
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
from nprrm.urls import urlpatterns
from components.models import Member, News


class PagesTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_pages(self):
        """ Test pages """

        for up in urlpatterns:
            if getattr(up, 'name', None) and not str(up.pattern).startswith('admin/'):
                response = self.client.get(reverse(up.name))
                self.assertEqual(response.status_code, 200)

    def test_news(self):
        """ Test news pages """

        qs = News.is_visible_objects.all()
        paginator = Paginator(qs, settings.PAGINATE_BY['NEWS'])
        for page in paginator.page_range:
            if page == 1:
                response = self.client.get(reverse('news_list'))
            else:
                response = self.client.get(
                    f"{reverse('news_list')}?page={page}")

            self.assertEqual(response.status_code, 200)

        response = self.client.get(f"{reverse('news_list')}?page=error")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"{reverse('news_list')}?page=1000")
        self.assertEqual(response.status_code, 404)

    def test_members_excluded(self):
        """ Test excluded members pages """

        qs = Member.is_visible_objects.filter(excluded=True)
        paginator = Paginator(qs, settings.PAGINATE_BY['DEFAULT'])
        for page in paginator.page_range:
            if page == 1:
                response = self.client.get(reverse('members_excluded_list'))
            else:
                response = self.client.get(
                    f"{reverse('members_excluded_list')}?page={page}")

            self.assertEqual(response.status_code, 200)

        response = self.client.get(f"{reverse('members_excluded_list')}?page=error")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"{reverse('members_excluded_list')}?page=1000")
        self.assertEqual(response.status_code, 404)

    def test_sitemap(self):
        """ Test sitemap page """

        response = self.client.get(
            reverse('django.contrib.sitemaps.views.sitemap'))
        self.assertEqual(response.status_code, 200)

    def test_page404(self):
        """ Test wrong page """

        response = self.client.get('test')
        self.assertEqual(response.status_code, 404)
