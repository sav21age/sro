from django.views.generic import DetailView
from django.http import Http404
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from django.conf import settings
from common.mixins import CacheMixin, CacheNewsMixin
from components.models import Member, News
from documents.models import (
    CompensationFund, DecisionMeeting, FederalLaw, FoundingDocument, Inspection,
    LocalRegulation, RegulatoryLegal, Reporting, TechnicalRegulation)
from files.models import File
from pages.models import (
    CompensationFundPage, ContactPage, DecisionMeetingPage, FederalLawPage, IndexPage,
    InspectionPage, JoinUsPage, LocalRegulationPage, MemberExcludedPage, MemberPage,
    NewsPage, PriorityDirectionPage, RegulatoryLegalPage, ReportingPage,
    TechnicalRegulationPage)
from pure_pagination.mixins import PaginationMixin


class IndexPageDetail(CacheMixin, DetailView):
    model = IndexPage
    template_name = 'index/index.html'

    def get_object(self, queryset=None):
        return IndexPage.is_visible_objects.get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['founding_document_list'] = FoundingDocument.is_visible_objects.all()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class PriorityDirectionPageDetail(CacheMixin, DetailView):
    model = PriorityDirectionPage
    template_name = 'priority-directions/detail.html'

    def get_object(self, queryset=None):
        return PriorityDirectionPage.is_visible_objects.get()

#--

class MemberPageList(CacheMixin, ListView):
    model = Member
    template_name = 'members/list.html'
    queryset = Member.is_visible_objects.filter(excluded=False) \
        .select_related('location') \
        .select_related('position') \
        .select_related('org_form')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = MemberPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class MemberExcludedPageList(PaginationMixin, CacheMixin, ListView):
    model = Member
    paginate_by = settings.PAGINATE_BY['DEFAULT']
    template_name = 'members/list.html'
    queryset = Member.is_visible_objects.filter(excluded=True) \
        .select_related('location') \
        .select_related('position') \
        .select_related('org_form')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = MemberExcludedPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404
        
        context['object'].excluded_flag = True

        return context

#--


class CompensationFundPageList(CacheMixin, ListView):
    model = CompensationFund
    template_name = 'compensation-fund/list.html'
    queryset = CompensationFund.is_visible_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = CompensationFundPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class InspectionPageList(CacheMixin, ListView):
    model = Inspection
    template_name = 'inspection/list.html'
    queryset = Inspection.is_visible_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = InspectionPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class DecisionMeetingPageList(CacheMixin, ListView):
    model = DecisionMeeting
    template_name = 'decision-meetings/list.html'
    queryset = DecisionMeeting.is_visible_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = DecisionMeetingPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class ReportingPageList(CacheMixin, ListView):
    model = Reporting
    template_name = 'reporting/list.html'

    def get_object(self, queryset=None):
        return Reporting.is_visible_objects.get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = ReportingPage.is_visible_objects\
                .prefetch_related('files') \
                .get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class NewsPageList(PaginationMixin, CacheNewsMixin, ListView):
    model = News
    paginate_by = settings.PAGINATE_BY['NEWS']
    template_name = 'news/list.html'
    # queryset = News.is_visible_objects.prefetch_related('files')
    queryset = News.is_visible_objects.prefetch_related(
        Prefetch(
            'files',
            queryset=File.is_visible_objects.all(),
            to_attr='is_visible_files'
        )
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = NewsPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class JoinUsPageDetail(CacheMixin, DetailView):
    model = JoinUsPage
    template_name = 'join-us/detail.html'

    def get_object(self, queryset=None):
        return JoinUsPage.is_visible_objects \
            .prefetch_related('files') \
            .get()

#--


class TechnicalRegulationPageList(CacheMixin, ListView):
    model = TechnicalRegulation
    template_name = 'technical-regulations/list.html'

    # def get_object(self, queryset=None):
    #     return Reporting.is_visible_objects.get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = TechnicalRegulationPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class FederalLawPageList(CacheMixin, ListView):
    model = FederalLaw
    template_name = 'federal-laws/list.html'

    # def get_object(self, queryset=None):
    #     return Reporting.is_visible_objects.get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = FederalLawPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class RegulatoryLegalPageList(CacheMixin, ListView):
    model = RegulatoryLegal
    template_name = 'regulatory-legal/list.html'

    # def get_object(self, queryset=None):
    #     return Reporting.is_visible_objects.get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = RegulatoryLegalPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context
#--


class LocalRegulationPageList(CacheMixin, ListView):
    model = LocalRegulation
    template_name = 'local-regulation/list.html'

    # def get_object(self, queryset=None):
    #     return Reporting.is_visible_objects.get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['object'] = LocalRegulationPage.is_visible_objects.get()
        except ObjectDoesNotExist:
            raise Http404

        return context

#--


class ContactPageDetail(CacheMixin, DetailView):
    model = ContactPage
    template_name = 'contacts/detail.html'
    # .select_related('brand')\
    # .prefetch_related('brand__images')\
    # .prefetch_related('features')

    # def get_queryset(self):
    #     return IndexPage.is_visible_objects.get()

    def get_object(self, queryset=None):
        return ContactPage.is_visible_objects.get()
