from datetime import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from common.managers import IsVisibleManager
from common.helpers import (
    get_doc_date_file_path, get_doc_name_file_path, get_doc_year_file_path,
    replace_quotes, document_extensions)


class SimplePage(models.Model):
    # is_visible = models.BooleanField('показывать?', default=1, db_index=True)

    head_title = models.CharField('title', max_length=80)
    meta_description = models.CharField('meta description', max_length=160)

    title = models.CharField('h1-заголовок', max_length=250)
    # slug = models.SlugField('url-адрес страницы', max_length=80, blank=False, unique=True)

    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True)

    # objects = models.Manager()
    # is_visible_objects = IsVisibleManager()

    def __str__(self):
        return self.title

    def clean(self):
        self.head_title = replace_quotes(self.head_title)
        self.meta_description = replace_quotes(self.meta_description)
        self.title = replace_quotes(self.title)
        super().clean()

    class Meta:
        abstract = True

# --


class TextPage(models.Model):
    text_top = models.TextField('текст', blank=True)
    text_bottom = models.TextField('текст', blank=True)

    class Meta:
        abstract = True

# --


class DocumentName(models.Model):
    is_visible = models.BooleanField('показывать?', default=1, db_index=True)

    name = models.TextField('название')
    file_path = models.FileField(
        'путь к файлу', upload_to=get_doc_name_file_path, max_length=140,
        validators=(FileExtensionValidator(document_extensions),)
    )
    file_size = models.CharField('размер файла', max_length=30, blank=True)

    # arc_path = models.FileField(
    #     'путь к архиву', blank=True, upload_to=get_file_path, max_length=250)
    # arc_size = models.CharField('размер архива', max_length=30, blank=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = True

# --


YEAR_CHOICES = []
for r in range(2015, (datetime.now().year+2)):
    YEAR_CHOICES.append((r, r))
YEAR_CHOICES.reverse()


class DocumentYear(models.Model):
    is_visible = models.BooleanField('показывать?', default=1, db_index=True)

    year = models.IntegerField(
        'год', choices=YEAR_CHOICES, default=datetime.now().year
    )

    file_path = models.FileField(
        'путь к файлу', upload_to=get_doc_year_file_path, max_length=140,
        validators=(FileExtensionValidator(document_extensions),)
    )
    file_size = models.CharField('размер файла', max_length=30, blank=True)

    # arc_path = models.FileField(
    #     'путь к архиву', blank=True)
    # # 'путь к архиву', blank=True, upload_to=get_report_file_path)
    # arc_size = models.CharField('размер архива', max_length=30, blank=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return str(self.year)

    class Meta:
        abstract = True

#--

class DocumentDate(models.Model):
    is_visible = models.BooleanField('показывать?', default=1, db_index=True)
    
    date = models.DateField('дата')
    name = models.CharField('название', max_length=200)
    
    file_path = models.FileField(
        'путь к файлу', upload_to=get_doc_date_file_path, max_length=140,
        validators=(FileExtensionValidator(document_extensions),)
    )
    file_size = models.CharField('размер файла', max_length=30, blank=True)

    # arc_path = models.FileField('путь к архиву', blank=True)
    # # 'путь к архиву', blank=True, upload_to=get_report_file_path)
    # arc_size = models.CharField('размер архива', max_length=30, blank=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return f'{self.name} от {self.date.strftime("%d.%m.%Y")} г.'
        
    class Meta:
        abstract = True
