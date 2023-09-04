import re
from django.core.exceptions import ValidationError


def FileExtValidator(value):
    if not re.match(r'.+\.(doc|docx|xls|xlsx|rtf|odt|pdf|djvu|xml)$', value.name) and re.match(r'^[\.]$', value.name):
        # raise ValidationError('Загружать можно только текстовые документы!')
        raise ValidationError('Можно загружать только *.doc, *.docx, *.xls, *.xlsx, *.rtf, *.odt, *.pdf, *.djvu, *.xml')