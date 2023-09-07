from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.core.paginator import Paginator
from django.conf import settings
from components.models import News
from pages.models import (
    CompensationFundPage, ContactPage, DecisionMeetingPage, FederalLawPage, InspectionPage,
    JoinUsPage, LocalRegulationPage, MemberPage, PriorityDirectionPage, RegulatoryLegalPage, 
    ReportingPage, TechnicalRegulationPage)


class IndexSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['index',]

    def location(self, item):
        return reverse('index')

#--


class PriorityDirectionSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['priority-directions']
        return PriorityDirectionPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('pd_detail')

#--


class CompensationFundSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['compensation-fund',]
        return CompensationFundPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('cf_list')

#--


class MemberSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['members',]
        return MemberPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('members_list')

#--


class InspectionSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['inspection',]
        return InspectionPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('inspection_list')

#--


class DecisionMeetingSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['decision-meetings',]
        return DecisionMeetingPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('dm_list')

#--


class ReportingSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['reporting',]
        return ReportingPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('reporting_list')

#--


class NewsSitemap(Sitemap):
    priority = 0.5

    def items(self):
        qs = News.objects.order_by('id').all()
        paginator = Paginator(qs, settings.PAGINATE_BY['NEWS'])
        return paginator.page_range

    def location(self, item):
        # return reverse('news_list', kwargs={'page': item})
        if item == 1:
            return reverse('news_list')
        return f"{reverse('news_list')}?page={item}"

#--


class JoinUsSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['join-us',]
        return JoinUsPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('join_us_detail')

#--


class TechnicalRegulationSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['technical-regulations',]
        return TechnicalRegulationPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('tr_list')

#--


class FederalLawSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['federal-laws',]
        return FederalLawPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('fl_list')

#--


class RegulatoryLegalSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['regulatory-legal',]
        return RegulatoryLegalPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('rl_list')

#--


class LocalRegulationSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['local-regulation',]
        return LocalRegulationPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('lr_list')

#--


class ContactSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['contacts',]
        return ContactPage.objects.order_by('id').all()

    def location(self, item):
        return reverse('contacts_detail')