#import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('stockInfo.xlsx')
worksheet = workbook.add_worksheet()
chartsheet = workbook.add_chartsheet()

chart = workbook.add_chart({"type": 'line'})
#chartsheet.set_chart(chart)

excel = ["A1","B1","C1","D1"]

marks = [
    ['Sagar',96.4],
    ['Eric',97],
    ['Steve',95.5],
    ['Ji Lin',99.1],
]

for x in range(0,len(marks)):
    worksheet.write_column(excel[x], marks[x])

chart.set_title({
    'name': 'Example Chart - School Marks',
})

chart.add_series({
    'values': '=Sheet1!$A$2:$D$2',
    'categories': '=Sheet1!$A$1:$D$1',
})

chart.set_x_axis({
    'name': 'Names',
    'name_font': {'size': 14, 'bold': True},
    'text_axis': True
})

chart.set_y_axis({
    'name': 'Mark',
    'name_font': {'size': 14, 'bold': True},
})

worksheet.insert_chart('A4', chart)

workbook.close()
