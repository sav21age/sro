import os
from django.http import HttpResponse
import reportlab
# from reportlab.rl_config import TTFSearchPath
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from nprrm.settings import BASE_DIR


def export_to_pdf(filename, title, data, table_col_widths):
    s = getSampleStyleSheet()
    s['Title'].fontName = 'Times New Roman Cyr Bold'
    s['Title'].fontSize = 10
    s['Title'].leading = 12

    fontName = 'Times New Roman Cyr'
    fontSize = 10

    s['Normal'].fontName = fontName
    s['Normal'].fontSize = fontSize

    s['BodyText'].fontName = fontName
    s['BodyText'].fontSize = fontSize
    s['BodyText'].alignment = 1

    s['Heading1'].fontName = fontName
    s['Heading1'].alignment = 1

    reportlab.rl_config.TTFSearchPath.append(os.path.join(BASE_DIR, 'static', 'fonts'))
    pdfmetrics.registerFont(TTFont('Times New Roman Cyr', 'timesnrcyrmt.ttf'))
    pdfmetrics.registerFont(TTFont('Times New Roman Cyr Bold', 'timesnrcyrmt_bold.ttf'))

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f"attachment; filename={filename}"

    doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []

    elements.append(Paragraph(title, s['Heading1']))

    for row, values in enumerate(data):
        for column, value in enumerate(values):
            if row == 0:
                data[row][column] = Paragraph(value, s["Title"])
            else:
                if column in [0, 6]:
                    data[row][column] = Paragraph(value, s["Normal"])
                else:
                    data[row][column] = Paragraph(value, s["BodyText"])

    table_style = TableStyle([
        ('BACKGROUND',(1,0),(1,0),colors.yellow),
        ('BACKGROUND',(4,0),(4,0),colors.yellow),
        ('BACKGROUND',(7,0),(7,0),colors.pink),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ])
    
    t = Table(data, table_col_widths)
    t.setStyle(table_style)

    elements.append(t)
    doc.build(elements)

    return response


    # def export_to_xls(self, request):
    #     buffer = io.BytesIO()
    #     workbook = xlsxwriter.Workbook(buffer)
    #     worksheet = workbook.add_worksheet()
    #     # worksheet.write('A1', 'Some Data')
    #     qs = self.model.objects.filter(excluded=False)
    #     columns = ('Регистрационный номер', 'Дата регистрации', 'Наименование организации', 'ИНН', 'ОГРН', 'Место нахождения', 'Должность и ФИО руководителя')
    #     bold = workbook.add_format({'bold': True})
    #     row_num = 0

    #     # Assign the titles for each cell of the header
    #     for col_num, column_title in enumerate(columns, 0):
    #         worksheet.write(row_num, col_num, column_title, bold)
    #         worksheet.set_column(row_num, col_num, len(column_title))
    #         # cell.value = column_title
    #         # cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=False)
    #         # cell.font = Font(bold=True)
    #     # Iterate through all coins
    #     for _, obj in enumerate(qs, 0):
    #         row_num += 1

    #         # Define the data for each cell in the row
    #         row = [
    #             obj.reg_num,
    #             obj.reg_date.strftime("%d-%m-%Y"),
    #             obj.org_form.fullname +' '+ obj.company_name,
    #             obj.inn, 
    #             obj.ogrn,
    #             obj.city.name,
    #             obj.position.name +' '+ obj.lastname +' '+ obj.firstname +' '+ obj.patronymic,
    #         ]

    #         # Assign the data for each cell of the row
    #         for col_num, cell_value in enumerate(row, 0):
    #             worksheet.write(row_num, col_num, cell_value)
    #             # cell = worksheet.cell(row=row_num, column=col_num)
    #             # cell.value = cell_value

    #     workbook.close()
    #     buffer.seek(0)

    #     return FileResponse(buffer, as_attachment=True, filename='report.xlsx')
    #     # self.model.objects.all().update(is_immortal=True)
    #     # self.message_user(request, "All heroes are now immortal")
    #     # return HttpResponseRedirect("../")