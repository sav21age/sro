from common.forms import DocumentNameAdminForm, DocumentDateAdminForm, DocumentYearAdminForm
from documents.models import (
    CompensationFund, DecisionMeeting, FederalLaw, FoundingDocument, Inspection,
    LocalRegulation, RegulatoryLegal, Reporting, SOUTResult, TechnicalRegulation)


class TechnicalRegulationAdminForm(DocumentNameAdminForm):
    class Meta(DocumentNameAdminForm.Meta):
        model = TechnicalRegulation

# --


class FederalLawAdminForm(DocumentNameAdminForm):
    class Meta(DocumentNameAdminForm.Meta):
        model = FederalLaw

# --


class RegulatoryLegalAdminForm(DocumentNameAdminForm):
    class Meta(DocumentNameAdminForm.Meta):
        model = RegulatoryLegal

# --


class LocalRegulationAdminForm(DocumentNameAdminForm):
    class Meta(DocumentNameAdminForm.Meta):
        model = LocalRegulation

# --


class CompensationFundAdminForm(DocumentNameAdminForm):
    class Meta(DocumentNameAdminForm.Meta):
        model = CompensationFund

# --


class FoundingDocumentAdminForm(DocumentNameAdminForm):
    class Meta(DocumentNameAdminForm.Meta):
        model = FoundingDocument

# --


class ReportingAdminForm(DocumentYearAdminForm):
    class Meta(DocumentYearAdminForm.Meta):
        model = Reporting

# --


class SOUTResultAdminForm(DocumentNameAdminForm):
    class Meta(DocumentNameAdminForm.Meta):
        model = SOUTResult

# --

# class FinancialStatementAdminForm(DocumentYearAdminForm):
#     class Meta(DocumentYearAdminForm.Meta):
#         model = FinancialStatement

# --

# class AuditReportAdminForm(DocumentYearAdminForm):
#     class Meta(DocumentYearAdminForm.Meta):
#         model = AuditReport

# --

# class ReportON0001AdminForm(DocumentYearAdminForm):
#     class Meta(DocumentYearAdminForm.Meta):
#         model = ReportON0001

# --

# class ReportON0002AdminForm(DocumentYearAdminForm):
#     class Meta(DocumentYearAdminForm.Meta):
#         model = ReportON0002

# --


class InspectionAdminForm(DocumentYearAdminForm):
    class Meta(DocumentYearAdminForm.Meta):
        model = Inspection

# --


class DecisionMeetingAdminForm(DocumentDateAdminForm):
    class Meta(DocumentDateAdminForm.Meta):
        model = DecisionMeeting
