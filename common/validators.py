import re
from django.core.exceptions import ValidationError


def DocumentExtValidator(value):
    if not re.match(r'.+\.(doc|docx|docm|xls|xlsx|xlsm|rtf|odt|pdf|djvu)$', value.name) and re.match(r'^[\.]$', value.name):
        raise ValidationError('Загружать можно только *.doc, *.docx, *.xls, *.xlsx, *.rtf, *.odt, *.pdf, *.djvu')
