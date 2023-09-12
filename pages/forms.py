from ckeditor.widgets import CKEditorWidget
from codemirror import CodeMirrorTextarea
from django import forms
from common.forms import SimplePageAdminForm, TextPageAdminForm
from pages.models import (
    CompensationFundPage, ContactPage, DecisionMeetingPage, FederalLawPage,
    IndexPage, InspectionPage, JoinUsPage, LocalRegulationPage, MemberPage,
    PriorityDirectionPage, RegulatoryLegalPage, ReportingPage, SOUTResultPage,
    TechnicalRegulationPage)


codemirror_widget = CodeMirrorTextarea(
    mode="xml",
    # theme="eclipse",
    # theme="neo",
    config={
        'fixedGutter': True,
        'lineWrapping': True,
        'matchBrackets': True,
        'htmlMode': True,
    },
)


class IndexPageAdminForm(SimplePageAdminForm):
    text = forms.CharField(label='Текст', required=False, widget=CKEditorWidget())
    struct = forms.CharField(label='Текст', required=False, widget=codemirror_widget)
    founders = forms.CharField(label='Текст', required=False, widget=CKEditorWidget())

    class Meta(SimplePageAdminForm.Meta):
        model = IndexPage

# --

class FoundingDocumentPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = CompensationFundPage

#--


class PriorityDirectionPageAdminForm(SimplePageAdminForm):
    # text = forms.CharField(label='Текст', required=False ,widget=codemirror_widget)
    text = forms.CharField(label='Текст', required=False, widget=CKEditorWidget())

    class Meta(SimplePageAdminForm.Meta):
        model = PriorityDirectionPage

# --


class MemberPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = MemberPage

# --


class MemberExcludedPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = MemberPage

# --


class CompensationFundPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = CompensationFundPage

# --


class InspectionPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = InspectionPage

# --


class DecisionMeetingPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = DecisionMeetingPage

# --

class ReportingPageAdminForm(SimplePageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = ReportingPage

# --


class SOUTResultPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = SOUTResultPage

# --


class JoinUsPageAdminForm(SimplePageAdminForm):
    text = forms.CharField(label='Текст', required=False, widget=CKEditorWidget())

    class Meta(SimplePageAdminForm.Meta):
        model = JoinUsPage
        
# --


class TechnicalRegulationPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = TechnicalRegulationPage

# --


class FederalLawPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = FederalLawPage

# --


class RegulatoryLegalPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = RegulatoryLegalPage

# --


class LocalRegulationPageAdminForm(SimplePageAdminForm, TextPageAdminForm):
    class Meta(SimplePageAdminForm.Meta):
        model = LocalRegulationPage

# --


class ContactPageAdminForm(SimplePageAdminForm):
    map = forms.CharField(label='Карта', required=False, widget=codemirror_widget)

    class Meta(SimplePageAdminForm.Meta):
        model = ContactPage
