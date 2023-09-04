import os
import re
import uuid
from pathlib import Path
from django.forms import NumberInput, Select, TextInput, Textarea
from django.db import models
from transliterate import translit


formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 50%;'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 30, 'style': 'width: 70%; font-size: 115%;'})},
    models.IntegerField: {'widget': NumberInput(attrs={'style': 'width: 100px;'})},
    models.DecimalField: {'widget': NumberInput(attrs={'style': 'width: 100px;'})},
    models.ForeignKey: {'widget': Select(attrs={'style': 'width: 250px;'})},
}

document_extensions = ('doc', 'docx', 'xls', 'xlsx', 'rtf', 'pdf', 'zip', '7z', 'rar', )

quote = re.compile(r'\"(.*?)\"')
quote_office = re.compile(r'\“(.*?)\”')

def replace_quotes(value):
    s = value.replace("'", '"').replace("“", '"').replace("”", '"')
    res = s.split('"')[1:]

    if len(res) > 1:
        res.pop()
        if len(res) == 1:
            return f"«{res[0]}»"
        elif len(res) == 2:
            return f"«{res[0]}«{res[1]}»"

    return value


def get_image_path(instance, filename):
    f = os.path.splitext(filename)
    fol = 'images'
    if hasattr(instance, 'upload_image_to'):
        fol = f'{fol}/{instance.upload_image_to}'
    return f'{fol}/{uuid.uuid1().hex}{f[1].lower()}'


# def get_file_path(instance, filename):
#     f = os.path.splitext(filename)
#     dir = 'files'
#     if hasattr(instance, 'upload_to'):
#         dir = '{0}/{1}'.format(dir, instance.upload_to)
#     return '{0}/{1}{2}'.format(dir, uuid.uuid1().hex, f[1].lower())

# import re
# s = "Свидетельство о государственной регистрации Ассоциации «РегионРемМонтаж ПБ» в Минюсте."
# s = re.sub("[^a-zA-Zа-яА-Я0-9 ]+", "", s)
# print(s)

def get_path_params(instance, filename):
    stem = Path(filename).stem
    stem = translit(stem, language_code='ru', reversed=True)
    stem = re.sub("[^-a-zA-Z0-9_ ]+", "", stem)
    stem = re.sub(r"\s+", ' ', stem)

    suffix = Path(filename).suffix
    fol = 'files'
    if hasattr(instance, 'upload_to'):
        fol = f"{fol}/{instance.upload_to}"

    return fol, stem[:120], suffix.lower()


def get_file_path(instance, filename):
    fol, stem, suffix = get_path_params(instance, filename)
    return f"{fol}/{stem}{suffix}"


def get_doc_name_file_path(instance, filename):
    fol, stem, suffix = get_path_params(instance, filename)
    return f"{fol}/{stem}{suffix}"


# #TODO: remove
# def get_year_file_path(instance, filename):
#     dir, stem, suffix = get_path_params(instance, filename)
#     return f"{dir}/{stem}{suffix}"


def get_doc_year_file_path(instance, filename):
    fol, stem, suffix = get_path_params(instance, filename)
    return f"{fol}/{stem}{suffix}"


# #Todo: remove
# def get_date_file_path(instance, filename):
#     dir, stem, suffix = get_path_params(instance, filename)
#     return f"{dir}/{instance.date}_{stem}{suffix}"


def get_doc_date_file_path(instance, filename):
    fol, stem, suffix = get_path_params(instance, filename)
    return f"{fol}/{instance.date}_{stem}{suffix}"


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
