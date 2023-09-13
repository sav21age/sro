import io
import os
from django.http import FileResponse, HttpResponse
from django.conf import settings
import reportlab
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
import xlsxwriter

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

    reportlab.rl_config.TTFSearchPath.append(os.path.join(settings.BASE_DIR, 'static', 'fonts'))
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
    table_col_widths[:] = [x * inch for x in table_col_widths]
    t = Table(data, table_col_widths)
    t.setStyle(table_style)

    elements.append(t)
    doc.build(elements)

    return response


def export_to_xls(filename, data, table_col_widths):
    buffer = io.BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': True, 'align': 'center',})
    bold_yellow = workbook.add_format({'bold': True, 'bg_color': 'yellow', 'align': 'center',})
    
    bold_pink = workbook.add_format({'bold': True, 'bg_color': 'pink', 'align': 'center',})
    
    wrap = workbook.add_format({'text_wrap': True, 'valign':'vcenter'})
    wrap_c = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign':'vcenter'})

    c = len(data)
    worksheet.ignore_errors({"number_stored_as_text": f"D2:D{c} E2:E{c}",})

    for index, lst in enumerate(data):
        for key, value in enumerate(lst):
            if index == 0:
                f = bold
                if key in [1,4]:
                    f = bold_yellow
                if key == 7:
                    f = bold_pink
                worksheet.write(index, key, value, f)

                # l = len(value)
                # if key == 6:
                #     l = l + 2
                worksheet.set_column(key, key, table_col_widths[key])
                # print(len(value))
            else:
                f = wrap_c
                if key in [0,6]:
                    f = wrap
                worksheet.write(index, key, value, f)

    workbook.close()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=filename)
