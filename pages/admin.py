from django.contrib import admin
from solo.admin import SingletonModelAdmin
from common.admin import SimplePageAdmin, TextPageAdmin
from files.admin import FileInline
from pages.forms import CompensationFundPageAdminForm, ContactPageAdminForm, DecisionMeetingPageAdminForm, FederalLawPageAdminForm, IndexPageAdminForm, InspectionPageAdminForm, JoinUsPageAdminForm, LocalRegulationPageAdminForm, MemberExcludedPageAdminForm, MemberPageAdminForm, PriorityDirectionPageAdminForm, RegulatoryLegalPageAdminForm, ReportingPageAdminForm, TechnicalRegulationPageAdminForm
from pages.models import CompensationFundPage, ContactPage, DecisionMeetingPage, FederalLawPage, IndexPage, InspectionPage, JoinUsPage, LocalRegulationPage, MemberExcludedPage, MemberPage, NewsPage, PriorityDirectionPage, RegulatoryLegalPage, ReportingPage, TechnicalRegulationPage

@admin.register(IndexPage)
class IndexPageAdmin(SimplePageAdmin, SingletonModelAdmin):
    # inlines = (FileInline,)
    form = IndexPageAdminForm

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('О компании', {
                'fields': ('text',)
            }),
            ('Структура', {
                'fields': ('struct',)
            }),
            ('Учредители', {
                'fields': ('founders',)
            }),
        )

#--


@admin.register(PriorityDirectionPage)
class PriorityDirectionPageAdmin(SimplePageAdmin, SingletonModelAdmin):
    form = PriorityDirectionPageAdminForm

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Текст', {
                'fields': ('text',)
            }),
        )

# --


@admin.register(MemberPage)
class MemberAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = MemberPageAdminForm

# --


@admin.register(MemberExcludedPage)
class MemberExcludedAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = MemberExcludedPageAdminForm


# --


@admin.register(CompensationFundPage)
class CompensationFundPageAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = CompensationFundPageAdminForm

# --


@admin.register(InspectionPage)
class InspectionPageAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = InspectionPageAdminForm

# --


@admin.register(DecisionMeetingPage)
class DecisionMeetingPageAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = DecisionMeetingPageAdminForm

# --


@admin.register(ReportingPage)
class ReportingPageAdmin(SimplePageAdmin, SingletonModelAdmin):
    form = ReportingPageAdminForm
    inlines = (FileInline,)

# --


@admin.register(NewsPage)
class NewsPageAdmin(SimplePageAdmin, SingletonModelAdmin):
    pass

# --


@admin.register(JoinUsPage)
class JoinUsPageAdmin(SimplePageAdmin, SingletonModelAdmin):
    inlines = (FileInline,)
    form = JoinUsPageAdminForm

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Текст', {
                'fields': ('text',)
            }),
        )

# --


@admin.register(TechnicalRegulationPage)
class TechnicalRegulationPageAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = TechnicalRegulationPageAdminForm

# --


@admin.register(FederalLawPage)
class FederalLawPageAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = FederalLawPageAdminForm

# --


@admin.register(RegulatoryLegalPage)
class RegulatoryLegalPageAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = RegulatoryLegalPageAdminForm

# --


@admin.register(LocalRegulationPage)
class LocalRegulationPageAdmin(SimplePageAdmin, TextPageAdmin, SingletonModelAdmin):
    form = LocalRegulationPageAdminForm

# --


@admin.register(ContactPage)
class ContactPageAdmin(SimplePageAdmin, SingletonModelAdmin):
    form = ContactPageAdminForm
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Контактная информация', {
                'fields': (
                    'contact_person',
                    'contact_position',
                    'phone',
                    'email',
                    'address',
                    'map',
                )
            }),
        )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['map'].widget.attrs['rows'] = 7
        form.base_fields['map'].widget.attrs['style'] = 'width: 90%;'
        return form
