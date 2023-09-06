from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from common.helpers import replace_quotes, get_file_path, document_extensions
from common.managers import IsVisibleManager


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
            self.name = replace_quotes(self.name)

        super().clean()

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'
