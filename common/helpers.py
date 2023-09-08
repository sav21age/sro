import re
from pathlib import Path
from django.forms import NumberInput, Select, TextInput, Textarea
from django.db import models
from transliterate import translit


formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 50%;'})},
    models.TextField: {'widget': Textarea(
        attrs={'rows': 30, 'style': 'width: 70%; font-size: 115%;'})
    },
    models.IntegerField: {'widget': NumberInput(attrs={'style': 'width: 100px;'})},
    models.DecimalField: {'widget': NumberInput(attrs={'style': 'width: 100px;'})},
    models.ForeignKey: {'widget': Select(attrs={'style': 'width: 250px;'})},
}

#--

document_extensions = ('doc', 'docx', 'xls', 'xlsx',
                       'rtf', 'pdf', 'zip', '7z', 'rar', )

#--

quote_double = re.compile(r'\"(.*?)\"')
quote_triple = re.compile(r'\"(.*?)\"(.*?)\"')

def replace_quotes(value):
    s = value.replace("'", '"').replace("“", '"').replace("”", '"')
    c = s.count('"')
    if c == 2:
        return re.sub(quote_double, r"«\1»", s)
    elif c == 3:
        return re.sub(quote_triple, r"«\1«\2»", s)

    return s

#--

def convert_bytes(num):
    """
    Convert bytes to KB... MB... GB... etc
    """
    for x in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if num < 1024.0:
            # return "%3.1f %s" % (num, x)
            return f"{num:.1f} {x}"
        num /= 1024.0

#--

# def get_image_path(instance, filename):
#     f = os.path.splitext(filename)
#     fol = 'images'
#     if hasattr(instance, 'upload_image_to'):
#         fol = f'{fol}/{instance.upload_image_to}'
#     return f'{fol}/{uuid.uuid1().hex}{f[1].lower()}'

#--

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


def get_doc_year_file_path(instance, filename):
    fol, stem, suffix = get_path_params(instance, filename)
    return f"{fol}/{stem}{suffix}"


def get_doc_date_file_path(instance, filename):
    fol, stem, suffix = get_path_params(instance, filename)
    return f"{fol}/{instance.date}_{stem}{suffix}"
