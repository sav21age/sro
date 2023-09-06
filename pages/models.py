from django.db import models
from django.contrib.contenttypes import fields
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save
from solo.models import SingletonModel
from files.models import File
from common.models import SimplePage, TextPage


class IndexPage(SimplePage, SingletonModel):
    text = models.TextField('текст', blank=True)
    struct = models.TextField('текст', blank=True)
    founders = models.TextField('текст', blank=True)
    # files = fields.GenericRelation(File)

    class Meta:
        verbose_name = 'главная страница'
        verbose_name_plural = 'главная страница'

# --


class PriorityDirectionPage(SimplePage, SingletonModel):
    text = models.TextField('текст', blank=True)

    class Meta:
        verbose_name = 'приоритетные направления'
        verbose_name_plural = 'приоритетные направления'

# --

class CompensationFundPage(SimplePage, TextPage, SingletonModel):
    class Meta:
        verbose_name = 'компенсационный фонд'
        verbose_name_plural = 'компенсационные фонды'

# --


class MemberPage(SimplePage, TextPage, SingletonModel):
    class Meta:
        verbose_name = 'реестр членов ассоциации'
        verbose_name_plural = 'реестр членов ассоциации'

# --


class MemberExcludedPage(SimplePage, TextPage, SingletonModel):
    class Meta:
        verbose_name = 'реестр исключенных членов ассоциации'
        verbose_name_plural = 'реестр исключенных членов ассоциации'

# --




class InspectionPage(SimplePage, TextPage, SingletonModel):
    class Meta:
        verbose_name = 'проверка организаций'
        verbose_name_plural = 'проверки организаций'

# --


class DecisionMeetingPage(SimplePage, TextPage, SingletonModel):
    class Meta:
        verbose_name = 'решения собраний'
        verbose_name_plural = 'решения собраний'

# --


class ReportingPage(SimplePage, SingletonModel):
    files = fields.GenericRelation(File)

    class Meta:
        verbose_name = 'отчетность'
        verbose_name_plural = 'отчетность'

# --


class NewsPage(SimplePage, SingletonModel):
    class Meta:
        verbose_name = 'новости'
        verbose_name_plural = 'новости'

# --


class JoinUsPage(SimplePage, SingletonModel):
    text = models.TextField('текст', blank=True)
    files = fields.GenericRelation(File)

    class Meta:
        verbose_name = 'вступить в СРО'
        verbose_name_plural = 'вступить в СРО'

# --


class TechnicalRegulationPage(SimplePage, TextPage, SingletonModel):
    class Meta:
        verbose_name = 'технические регламенты'
        verbose_name_plural = 'технические регламенты'

# --


class FederalLawPage(SimplePage, TextPage,  SingletonModel):
    class Meta:
        verbose_name = 'федеральные законы'
        verbose_name_plural = 'федеральные законы'

# --


class RegulatoryLegalPage(SimplePage, TextPage,  SingletonModel):
    class Meta:
        verbose_name = 'нормативно-правовые документы'
        verbose_name_plural = 'нормативно-правовые документы'

# --


class LocalRegulationPage(SimplePage, TextPage,  SingletonModel):
    class Meta:
        verbose_name = 'локальные нормативные акты'
        verbose_name_plural = 'локальные нормативные акты'

# --


class ContactPage(SimplePage, SingletonModel):
    phone = models.CharField('телефон', max_length=20, null=True, blank=True)
    contact_person = models.CharField(
        'контактное лицо', max_length=200, null=True, blank=True)
    contact_position = models.CharField(
        'должность контактного лица', max_length=200, null=True, blank=True)
    email = models.CharField('email', max_length=50, null=True, blank=True)
    address = models.CharField('адрес', max_length=200, null=True, blank=True)
    map = models.TextField('карта', null=True, blank=True)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'

# --


@receiver(post_save, sender=IndexPage)
@receiver(post_save, sender=PriorityDirectionPage)
@receiver(post_save, sender=MemberPage)
@receiver(post_save, sender=MemberExcludedPage)
@receiver(post_save, sender=CompensationFundPage)
@receiver(post_save, sender=InspectionPage)
@receiver(post_save, sender=DecisionMeetingPage)
@receiver(post_save, sender=ReportingPage)
@receiver(post_save, sender=NewsPage)
@receiver(post_save, sender=JoinUsPage)
@receiver(post_save, sender=TechnicalRegulationPage)
@receiver(post_save, sender=FederalLawPage)
@receiver(post_save, sender=RegulatoryLegalPage)
@receiver(post_save, sender=LocalRegulationPage)
@receiver(post_save, sender=ContactPage)
def cache_invalidate(instance, **kwargs):
    if kwargs.get('raw'):  # add for test, pass fixtures
        return

    cache.clear()
