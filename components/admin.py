from django.contrib import admin
from django.urls import path
from django.utils.safestring import mark_safe
from reportlab.lib.units import inch
from components.export import export_to_pdf
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

#--


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

#--


@admin.register(OrgForm)
class OrgFormAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

#--


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('files')

    inlines = (FileInline,)
    list_display = ('get_date', 'get_description', 'get_files')

    @admin.display(description='есть файлы?', boolean=True)
    def get_files(self, obj=None):
        if obj.files.all():
            return True
        return False

    @admin.display(description='дата')
    def get_date(self, obj=None):
        return obj.date.strftime("%d.%m.%Y")

    def get_description(self, obj=None):
        if obj.description:
            return obj.description
        return "-"
    get_description.short_description = 'описание'

#--


class MemberAdmin(admin.ModelAdmin):
    change_list_template = "members/admin/change-list.html"

    list_display = ('get_reg_num_nowrap', 'get_fullname', 'get_shortname', 'excluded',)
    list_filter = ('excluded', )
    search_fields = ('inn', 'ogrn', 'company_fullname', 'company_shortname', 'lastname',)
    search_help_text = 'Поиск по ИНН, ОГРН, названию компании и фамилии'
    formfield_overrides = formfield_overrides
    save_on_top = True

    def get_reg_num_nowrap(self, obj=None):
        return mark_safe(f'<span style="white-space: nowrap;">{obj.reg_num}</span>')
    get_reg_num_nowrap.short_description = 'рег. №'

    def get_fullname(self, obj=None):
        return obj.get_company_fullname
        # if not obj.company_fullname:
        #     return f"{obj.org_form} {obj.lastname} {obj.firstname} {obj.patronymic}"
        # else:
        #     return f"{obj.org_form} {obj.company_fullname}"
    get_fullname.short_description = 'полное название компании'

    def get_shortname(self, obj=None):
        return obj.get_company_shortname
        # if not obj.company_shortname:
        #     return f"{obj.org_form} {obj.lastname} {obj.firstname} {obj.patronymic}"
        # else:
        #     return f"{obj.org_form} {obj.company_shortname}"
    get_shortname.short_description = 'сокращенное название компании'


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
            row.append(f"{obj.org_form.fullname} {obj.company_fullname}" + "<br/>\n" + f"({obj.org_form.shortname} {obj.company_shortname})")
            row.append(obj.inn)
            row.append(obj.ogrn)
            row.append(obj.location.name)
            row.append(f"{obj.position.name} {obj.lastname} {obj.firstname} {obj.patronymic}")
            data.append(row)

        table_col_widths = (1.7*inch, 0.95*inch, 2.65*inch, 0.9*inch, 1.1*inch, 1.5*inch, 2.0*inch)

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
            row.append(f"{obj.org_form.fullname} {obj.company_fullname} <br/>\n ({obj.org_form.shortname} {obj.company_shortname})")
            row.append(obj.inn)
            row.append(obj.ogrn)
            row.append(obj.location.name)
            row.append(f"{obj.position.name} <br/>\n {obj.lastname} {obj.firstname} {obj.patronymic}")
            row.append(obj.excluded_date.strftime("%d.%m.%Y"))
            data.append(row)

        table_col_widths = (1.7*inch, 0.95*inch, 2.25*inch, 0.9*inch, 1.1*inch, 1.5*inch, 1.4*inch, 1.0*inch)

        return export_to_pdf("registry-of-excluded-members.pdf", title, data, table_col_widths)

admin.site.register(Member, MemberAdmin)