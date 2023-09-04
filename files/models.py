import re
from django.db import models
from common.helpers import quote, quote_office
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from common.helpers import get_file_path
from common.managers import IsVisibleManager
from django.core.validators import FileExtensionValidator
from common.helpers import document_extensions


class File(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    is_visible = models.BooleanField('показывать', default=1, db_index=True)

    name = models.CharField('название', max_length=250)
    path = models.FileField('Путь к документу', max_length=250, upload_to=get_file_path,
        validators=(FileExtensionValidator(document_extensions),)
    )

    # CHOICES = (
    #     ('', 'None'),
    #     ('DM', 'Решения собраний'),
    # )
    # purpose = models.CharField('назначение', max_length=2, choices=CHOICES, default='', blank=True)


    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return str(self.path)
    
    def clean(self):
        if self.name:
            self.name = re.sub(quote, r"«\1»", self.name)
            self.name = re.sub(quote_office, r"«\1»", self.name)

        super().clean()

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'