# import re
# from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


IsNumericValidator = RegexValidator(r'^[0-9+]', 'Можно вводить только цифры.')

# def DocumentExtValidator(value):
#     if not re.match(r'.+\.(doc|docx|docm|xls|xlsx|xlsm|rtf|odt|pdf|djvu)$', value.name) and re.match(r'^[\.]$', value.name):
#         raise ValidationError('Загружать можно только *.doc, *.docx, *.xls, *.xlsx, *.rtf, *.odt, *.pdf, *.djvu')
    
