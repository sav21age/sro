from django.db import models
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from common.models import DocumentDate, DocumentName, DocumentYear
from common.signals import receiver_multiple


class FoundingDocument(DocumentName):
    upload_to = 'founding-documents'

    class Meta:
        ordering = ('id',)
        verbose_name = 'учредительный документ'
        verbose_name_plural = 'учредительные документы'

# --


class CompensationFund(DocumentName):
    upload_to = 'compensation-fund'

    class Meta:
        ordering = ('id',)
        verbose_name = 'документы компенсационного фонда'
        verbose_name_plural = 'документы компенсационного фонда'

# --


class Inspection(DocumentYear):
    upload_to = 'inspection'

    class Meta:
        ordering = ('-year',)
        verbose_name = 'проверка организаций'
        verbose_name_plural = 'проверки организаций'
        constraints = [
            models.UniqueConstraint(fields=('year',), name='unique year')
        ]

# --


class DecisionMeeting(DocumentDate):
    upload_to = 'decision-meetings'

    class Meta:
        ordering = ('-date', '-id', )
        unique_together = ('date', 'name',)
        verbose_name = 'решение собрания'
        verbose_name_plural = 'решения собраний'

# --


class Reporting(DocumentYear):
    CHOICES = (
        ('', '-----'),
        ('financial-statements', 'Бухгалтерская отчетность'),
        ('audit-reports', 'Аудиторское заключение'),
        ('on0001-reports', 'Отчет по форме №ОН0001'),
        ('on0002-reports', 'Отчет по форме №ОН0002'),
    )
    # purpose = models.CharField(null=True, blank=True)
    upload_to = models.CharField(
        'тип документа', max_length=30, choices=CHOICES)

    class Meta:
        ordering = ('-year',)
        unique_together = ('year', 'upload_to',)
        verbose_name = 'отчетность'
        verbose_name_plural = 'отчетность'

# --


class SOUTResult(DocumentName):
    upload_to = 'sout-result'

    class Meta:
        verbose_name = 'результаты проведения СОУТ'
        verbose_name_plural = 'результаты проведения СОУТ'

# --


class TechnicalRegulation(DocumentName):
    upload_to = 'technical-regulations'

    class Meta:
        ordering = ('-id',)
        verbose_name = 'технический регламент'
        verbose_name_plural = 'технические регламенты'

# --


class FederalLaw(DocumentName):
    upload_to = 'federal-laws'

    class Meta:
        ordering = ('-id',)
        verbose_name = 'федеральный закон'
        verbose_name_plural = 'федеральные законы'

# --


class RegulatoryLegal(DocumentName):
    upload_to = 'regulatory-legal'

    class Meta:
        ordering = ('-id',)
        verbose_name = 'нормативно-правовой документ'
        verbose_name_plural = 'нормативно-правовые документы'

# --


class LocalRegulation(DocumentName):
    upload_to = 'local-regulations'

    class Meta:
        ordering = ('-id',)
        verbose_name = 'локальный нормативный акт'
        verbose_name_plural = 'локальные нормативные акты'

# --


senders = [
    FoundingDocument, CompensationFund, Inspection, DecisionMeeting,
    Reporting, SOUTResult, TechnicalRegulation, FederalLaw, RegulatoryLegal, 
    LocalRegulation,
]
@receiver_multiple(post_save, senders)
@receiver_multiple(post_delete, senders)
def cache_invalidate(instance, **kwargs):
    if kwargs.get('raw'):  # add for test, pass fixtures
        return

    cache.clear()
