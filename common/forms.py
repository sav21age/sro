from django import forms
from common.models import SimplePage, TextPage
from ckeditor.widgets import CKEditorWidget


class SimplePageAdminForm(forms.ModelForm):
    class Meta:
        model = SimplePage
        widgets = {
            'meta_description': forms.Textarea(attrs={'rows': 3, 'style': 'width: 70%;'}),
            'title': forms.Textarea(attrs={'rows': 3, 'style': 'width: 70%;'}),
        }
        exclude = []

#--


class TextPageAdminForm(forms.ModelForm):
    text_top = forms.CharField(label='Текст', required=False, widget=CKEditorWidget())
    text_bottom = forms.CharField(label='Текст', required=False, widget=CKEditorWidget())

    class Meta:
        model = TextPage
        exclude = []

#--


class DocumentNameAdminForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['arc_path'].widget.attrs['disabled'] = 'disabled'
    #         # self.fields['arc_path'].widget.attrs['readonly'] = True
    #     else:
    #         self.fields['arc_path'].widget = forms.HiddenInput()

    class Meta:
        # exclude = ('file_size', 'arc_size', )
        exclude = ('file_size',)

#--

class DocumentYearAdminForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['arc_path'].widget.attrs['disabled'] = 'disabled'
    #         # self.fields['arc_path'].widget.attrs['readonly'] = True
    #     else:
    #         self.fields['arc_path'].widget = forms.HiddenInput()

    class Meta:
        # exclude = ('file_size', 'arc_size', )
        exclude = ('file_size',)

#--

class DocumentDateAdminForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['arc_path'].widget.attrs['disabled'] = 'disabled'
    #         # self.fields['arc_path'].widget.attrs['readonly'] = True
    #     else:
    #         self.fields['arc_path'].widget = forms.HiddenInput()

    class Meta:
        # exclude = ('file_size', 'arc_size', )
        exclude = ('file_size',)

