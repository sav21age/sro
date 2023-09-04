from django import forms
from files.models import File


class FileAdminForm(forms.ModelForm):
    class Meta:
        model = File
        widgets = {
            'name': forms.Textarea(attrs={'rows': 3, 'style': 'width: 70%;'}),
        }
        exclude = []