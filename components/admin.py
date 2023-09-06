from django.contrib import admin
from django.urls import path
from django.utils.safestring import mark_safe
from components.export import export_to_pdf
from components.forms import NewsAdminForm
from components.models import Location, Member, News, OrgForm, Position
from files.admin import FileInline
from common.helpers import formfield_overrides


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

# --


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

# --


@admin.register(OrgForm)
class OrgFormAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

# --


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('files')

    inlines = (FileInline,)
    list_display = ('get_date', 'is_visible', 'get_description', 'get_files')
    form = NewsAdminForm
    save_on_top = True

    @admin.display(description='содержит файлы?', boolean=True)
    def get_files(self, obj=None):
        if obj.files.all():
            return True
        return False

    @admin.display(description='дата')
    def get_date(self, obj=None):
        return obj.date.strftime("%d.%m.%Y")
    get_date.admin_order_field = 'date'

    def get_description(self, obj=None):
        if obj.description:
            return mark_safe(obj.description)
        return "-"
    get_description.short_description = 'описание'

# --


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    change_list_template = "members/admin/change-list.html"

    list_display = ('reg_num', 'get_shortname', 'excluded',)
    list_filter = ('excluded', )
    search_fields = ('reg_num', 'company_fullname', 'company_shortname',)
    search_help_text = 'Поиск по: рег. № и сокращенному названию компании'
    formfield_overrides = formfield_overrides
    save_on_top = True

    # def get_reg_num_nowrap(self, obj=None):
    #     return mark_safe(f'<span style="white-space: nowrap;">{obj.reg_num}</span>')
    # get_reg_num_nowrap.short_description = 'рег. №'
    # get_reg_num_nowrap.admin_order_field = 'reg_num'

    def get_fullname(self, obj=None):
        return obj.get_company_fullname
    get_fullname.short_description = 'полное название компании'

    def get_shortname(self, obj=None):
        return obj.get_company_shortname
    get_shortname.short_description = 'сокращенное название компании'
    get_shortname.admin_order_field = 'company_shortname'

    def get_urls(self):
        urls = super().get_urls()
        export_urls = [
            path('export-members/', self.export_members),
            path('export-excluded-members/', self.export_excluded_members),
        ]
        return export_urls + urls

    def export_members(self, request):
        title = 'Реестр членов Ассоциации "РегионРемМонтаж ПБ"'

        data = [
            ['Регистрационный номер',
             'Дата регистрации',
             'Наименование организации',
             'ИНН',
             'ОГРН',
             'Место нахождения',
             'Должность и ФИО руководителя'],
        ]

        qs = self.model.objects.filter(excluded=False)
        for obj in qs:
            row = []
            row.append(obj.reg_num)
            row.append(obj.reg_date.strftime("%d.%m.%Y"))
            row.append(f"{obj.org_form.fullname} {obj.company_fullname}" +
                       "<br/>\n" + f"({obj.org_form.shortname} {obj.company_shortname})")
            row.append(obj.inn)
            row.append(obj.ogrn)
            row.append(obj.location.name)
            row.append(
                f"{obj.position.name} {obj.lastname} {obj.firstname} {obj.patronymic}")
            data.append(row)

        table_col_widths = (1.7, 0.95, 2.65, 0.9, 1.1, 1.5, 2.0) #in inch

        return export_to_pdf("registry-of-members.pdf", title, data, table_col_widths)

    def export_excluded_members(self, request):
        title = 'Реестр исключенных членов Ассоциации "РегионРемМонтаж ПБ"'

        data = [
            ['Регистрационный номер',
             'Дата регистрации',
             'Наименование организации',
             'ИНН',
             'ОГРН',
             'Место нахождения',
             'Должность и ФИО руководителя',
             'Дата прекращения',],
        ]

        qs = self.model.objects.filter(excluded=True)
        for obj in qs:
            row = []
            row.append(obj.reg_num)
            row.append(obj.reg_date.strftime("%d.%m.%Y"))
            row.append(f"{obj.org_form.fullname} {obj.company_fullname}" + 
                       "<br/>\n" + f"({obj.org_form.shortname} {obj.company_shortname})")
            row.append(obj.inn)
            row.append(obj.ogrn)
            row.append(obj.location.name)
            row.append(
                f"{obj.position.name} <br/>\n {obj.lastname} {obj.firstname} {obj.patronymic}")
            row.append(obj.excluded_date.strftime("%d.%m.%Y"))
            data.append(row)

        table_col_widths = (1.7, 0.95, 2.25, 0.9, 1.1, 1.5, 1.4, 1.0)

        return export_to_pdf("registry-of-excluded-members.pdf", title, data, table_col_widths)
