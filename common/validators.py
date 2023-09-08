from django.core.validators import RegexValidator

IsNumericValidator = RegexValidator(r'^[0-9+]', 'Можно вводить только цифры.')
