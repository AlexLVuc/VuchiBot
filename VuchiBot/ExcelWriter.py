#import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('stockInfo.xlsx')
worksheet = workbook.add_worksheet()
chartsheet = workbook.add_chartsheet()

chart = workbook.add_chart({"type": 'line'})
#chartsheet.set_chart(chart)

excel = ["A","B","C","D","E","F","G","H","I","J"]

marks = [
    ['Sagar',96.4],
    ['Eric',97],
    ['Steve',95.5],
    ['Ji Lin',99.1],
    ['Alex', 94.4],
    ['Gaurav', 96],
    ['Yash', 98],
]

for x in range(0,len(marks)):
    worksheet.write_column(excel[x] + '1', marks[x])

chart.set_title({
    'name': 'Example Chart - School Marks',
})

chart.add_series({
    'name': 'School Marks',
    'values': '=Sheet1!$' + excel[0] + '$2:' + excel[len(marks)] + '$2',
    'categories': '=Sheet1!$' + excel[0] + '$1:' + excel[len(marks)] + '$1',
    'marker': {'type': 'diamond'},
    'trendline': {
        'name': 'Average',
        'type': 'moving_average',
        'period': 1,
    },
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
