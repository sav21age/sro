from pathlib import Path
from django.contrib import admin
from common.forms import SimplePageAdminForm
from common.helpers import convert_bytes, formfield_overrides
# from zipfile import ZipFile
# from django.core.files.base import ContentFile


# https://stackoverflow.com/questions/58256151/set-ordering-of-apps-and-models-in-django-admin-dashboard
def get_app_list(self, request, app_label=None):
    """
    Return a sorted list of all the installed apps that have been
    registered in this site.
    """
    app_dict = self._build_app_dict(request, app_label)

    # Sort the apps alphabetically.
    app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

    return app_list

admin.AdminSite.get_app_list = get_app_list

#--


class SimplePageAdmin(admin.ModelAdmin):
    save_on_top = True
    form = SimplePageAdminForm
    formfield_overrides = formfield_overrides
    fieldsets = (
        # ('', {
        #     'fields': ('is_visible',)
        # }),
        ('Мета теги страницы и заголовок', {
            'fields': ('head_title', 'meta_description', 'title',)
        }),
    )

#--


class TextPageAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Текст (верх)', {
                'fields': ('text_top',)
            }),
            ('Текст (низ)', {
                'fields': ('text_bottom',)
            }),
        )

# class FilePathAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)

#         if 'file_path' in form.changed_data:
#             if obj.file_path.path:
#                 stem = Path(obj.file_path.path).stem
#                 arc_path = Path.joinpath(
#                     Path(obj.file_path.path).parent, f"{stem}.zip")

#                 obj.arc_path.save(arc_path, ContentFile(''))
#                 with ZipFile(obj.arc_path.path, 'w') as arc:
#                     pass

#                 with ZipFile(obj.arc_path.path, 'w') as arc:
#                     arc.write(obj.file_path.path, arcname=Path(
#                         obj.file_path.path).name)

#                 size = Path(obj.file_path.path).stat().st_size
#                 obj.file_size = convert_bytes(size)

#                 size = Path(obj.arc_path.path).stat().st_size
#                 obj.arc_size = convert_bytes(size)

#         super().save_model(request, obj, form, change)


class FilePathAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if 'file_path' in form.changed_data:
            if obj.file_path.path:
                try:
                    size = Path(obj.file_path.path).stat().st_size
                    size = convert_bytes(size)
                except FileNotFoundError:
                    size = 0

                obj.file_size = size

        super().save_model(request, obj, form, change)


class DocumentNameAdmin(FilePathAdmin):
    list_display = ('name',)


class DocumentYearAdmin(FilePathAdmin):
    list_display = ('year',)


class DocumentDateAdmin(FilePathAdmin):
    list_display = ('date',)
