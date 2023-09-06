from django.db import models
from django.contrib.contenttypes import fields
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save
from common.helpers import replace_quotes
from common.managers import IsVisibleManager
from common.validators import IsNumericValidator
from files.models import File


class Location(models.Model):
    name = models.CharField('название', max_length=100, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'место нахождения'
        verbose_name_plural = 'место нахождения'

# --


class Position(models.Model):
    name = models.CharField('название', max_length=100, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'

# --


class OrgForm(models.Model):
    shortname = models.CharField('сокращенное название', max_length=10)
    fullname = models.CharField('полное название', max_length=100)

    def __str__(self):
        return str(self.shortname)

    class Meta:
        verbose_name = 'форма организации'
        verbose_name_plural = 'формы организации'

# --


class News(models.Model):
    is_visible = models.BooleanField('показывать?', default=1, db_index=True)

    date = models.DateField('дата')
    description = models.TextField('описание', blank=True)
    files = fields.GenericRelation(File)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return str(self.date)

    class Meta:
        unique_together = ('date', 'description',)
        ordering = ('-date', )
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

# --


class Member(models.Model):
    is_visible = models.BooleanField('показывать?', default=1, db_index=True)

    reg_num = models.CharField(
        'рег. №', unique=True, db_index=True, max_length=25)
    reg_date = models.DateField('дата регистрации')
    inn = models.CharField('ИНН', max_length=12, unique=True, db_index=True, validators=[
                           MinLengthValidator(10), IsNumericValidator])
    ogrn = models.CharField('ОГРН', max_length=13, unique=True, db_index=True, validators=[
                            MinLengthValidator(13), IsNumericValidator])

    # city = models.ForeignKey(City, verbose_name='город', on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, verbose_name='место нахождения', on_delete=models.CASCADE)

    org_form = models.ForeignKey(
        OrgForm, verbose_name='форма организации', on_delete=models.CASCADE)
    company_fullname = models.CharField(
        'полное название компании', max_length=250, blank=True, db_index=True,
        help_text='например: "Самая Лучшая Компания"',
    )
    company_shortname = models.CharField(
        'сокращенное название компании', max_length=250, blank=True, db_index=True,
        help_text='например: "СЛК"',
    )
    position = models.ForeignKey(
        Position, verbose_name='должность', blank=True, null=True, on_delete=models.CASCADE)
    lastname = models.CharField('фамилия', max_length=100, db_index=True)
    firstname = models.CharField('имя', max_length=100)
    patronymic = models.CharField('отчество', max_length=100)

    # founder = models.BooleanField('учредитель ассоциации', default=False, blank=True)
    excluded = models.BooleanField(
        'исключен из ассоциации?', default=False, db_index=True)
    excluded_date = models.DateField('дата исключения', blank=True, null=True)
    # excluded_decision = models.ForeignKey(DecisionMeeting, verbose_name='исключен решением собрания', blank=True, null=True, on_delete=models.CASCADE)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    @property
    def get_company_fullname(self):
        if not self.company_fullname:
            return f"{self.org_form} {self.lastname} {self.firstname} {self.patronymic}"
        else:
            return f"{self.org_form} {self.company_fullname}"

    @property
    def get_company_shortname(self):
        if not self.company_shortname:
            return f"{self.org_form} {self.lastname} {self.firstname} {self.patronymic}"
        else:
            return f"{self.org_form} {self.company_shortname}"

    def __str__(self):
        return self.get_company_fullname

    def clean(self):
        self.reg_num = self.reg_num.strip().replace('–', '-')
        self.company_fullname = replace_quotes(self.company_fullname)
        self.company_shortname = replace_quotes(self.company_shortname)

        msg_required = 'Обязательное поле.'
        if self.excluded:
            # if not self.excluded_date and not self.excluded_decision:
            # raise ValidationError({
            #     'excluded_date': ValidationError(msg_required, code='required'),
            #     'excluded_decision': ValidationError(msg_required, code='required'),
            # })

            if not self.excluded_date:
                raise ValidationError(
                    {'excluded_date': msg_required}, code='required')

            # if not self.excluded_decision:
            #     raise ValidationError({'excluded_decision': msg_required}, code='required')
        else:
            msg_excluded = 'Поле "Исключен из ассоциации?" не отмечено.'
            # if self.excluded_date or self.excluded_decision:
            #     raise ValidationError({
            #         'excluded_date': ValidationError(msg_excluded),
            #         'excluded_decision': ValidationError(msg_excluded),
            #     })

            if self.excluded_date:
                raise ValidationError(
                    {'excluded_date': msg_excluded}, code='required')

            # self.excluded_date = None
            # self.excluded_decision = None

        if self.company_fullname and not self.company_shortname:
            raise ValidationError(
                {'company_shortname': msg_required}, code='required')

        if self.company_shortname and not self.company_fullname:
            raise ValidationError(
                {'company_fullname': msg_required}, code='required')

        super().clean()

    class Meta:
        ordering = ('reg_num', )
        verbose_name = 'член ассоциации'
        verbose_name_plural = 'члены ассоциации'

# --


@receiver(post_save, sender=Location)
@receiver(post_save, sender=Position)
@receiver(post_save, sender=OrgForm)
@receiver(post_save, sender=News)
@receiver(post_save, sender=Member)
def cache_invalidate(instance, **kwargs):
    if kwargs.get('raw'):  # add for test, pass fixtures
        return

    cache.clear()
