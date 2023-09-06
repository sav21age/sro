from django import forms
from ckeditor.widgets import CKEditorWidget
from components.models import News


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Текст', required=False, widget=CKEditorWidget())

    class Meta:
        model = News
        exclude = []