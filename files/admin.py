from common.helpers import formfield_overrides
from django.contrib.contenttypes.admin import GenericStackedInline
from files.forms import FileAdminForm
from files.models import File

class FileInline(GenericStackedInline):
    model = File
    form = FileAdminForm
    extra = 0
    show_change_link = True
    formfield_overrides = formfield_overrides
    verbose_name = "файл"
    verbose_name_plural = "файлы"
