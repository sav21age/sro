from django.contrib import admin
from common.admin import DocumentNameAdmin, DocumentDateAdmin, DocumentYearAdmin
from documents.forms import (
    CompensationFundAdminForm, DecisionMeetingAdminForm, FederalLawAdminForm,
    FoundingDocumentAdminForm, InspectionAdminForm, LocalRegulationAdminForm,
    RegulatoryLegalAdminForm, ReportingAdminForm, TechnicalRegulationAdminForm)
from documents.models import (
    CompensationFund, DecisionMeeting, FederalLaw, FoundingDocument, Inspection,
    LocalRegulation, RegulatoryLegal, Reporting, TechnicalRegulation)


@admin.register(FoundingDocument)
class FoundingDocumentAdmin(DocumentNameAdmin):
    form = FoundingDocumentAdminForm

#--


@admin.register(CompensationFund)
class CompensationFundAdmin(DocumentNameAdmin):
    form = CompensationFundAdminForm


#--


@admin.register(Inspection)
class InspectionAdmin(DocumentYearAdmin):
    form = InspectionAdminForm
# --


@admin.register(DecisionMeeting)
class DecisionMeetingAdmin(DocumentDateAdmin):
    form = DecisionMeetingAdminForm
    list_display = ('date', 'name',)
    # formfield_overrides = formfield_overrides

#--


@admin.register(Reporting)
class ReportingAdmin(DocumentYearAdmin):
    list_display = ('year', 'upload_to',)
    list_filter = ('upload_to',)
    form = ReportingAdminForm

#--


@admin.register(TechnicalRegulation)
class TechnicalRegulationAdmin(DocumentNameAdmin):
    form = TechnicalRegulationAdminForm


# --

@admin.register(FederalLaw)
class FederalLawAdmin(DocumentNameAdmin):
    form = FederalLawAdminForm


# --

@admin.register(RegulatoryLegal)
class RegulatoryLegalAdmin(DocumentNameAdmin):
    form = RegulatoryLegalAdminForm


# --


@admin.register(LocalRegulation)
class LocalRegulationAdmin(DocumentNameAdmin):
    form = LocalRegulationAdminForm


