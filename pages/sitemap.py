from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class IndexSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['index',]

    def location(self, item):
        return reverse('index')


class PriorityDirectionSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['priority-directions']

    def location(self, item):
        return reverse('pd_detail')


class CompensationFundSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['compensation-fund',]

    def location(self, item):
        return reverse('cf_list')


class MemberPageSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['members',]

    def location(self, item):
        return reverse('members_list')


class DecisionMeetingSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['decision-meetings',]

    def location(self, item):
        return reverse('dm_list')


class InspectionSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['inspection',]

    def location(self, item):
        return reverse('inspection_list')


class ReportingSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['reporting',]

    def location(self, item):
        return reverse('reporting_list')


class NewsSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['news',]

    def location(self, item):
        return reverse('news_list')


class JoinUsSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['join-us',]

    def location(self, item):
        return reverse('join_us_detail')


class TechnicalRegulationSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['technical-regulations',]

    def location(self, item):
        return reverse('tr_list')


class FederalLawSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['federal-laws',]

    def location(self, item):
        return reverse('fl_list')


class RegulatoryLegalSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['regulatory-legal',]

    def location(self, item):
        return reverse('rl_list')


class LocalRegulationSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['local-regulation',]

    def location(self, item):
        return reverse('lr_list')


class ContactSitemap(Sitemap):
    priority = 1

    def items(self):
        return ['contacts',]

    def location(self, item):
        return reverse('contacts_detail')
