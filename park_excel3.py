import xlsxwriter

workbook = xlsxwriter.Workbook('park3.xlsx')
worksheet = workbook.add_worksheet("My sheet")

cell_format = workbook.add_format({'font_color': 'black'})
cell_format.set_align('center')

worksheet.write('A1', 'Rs.0.0', cell_format)
worksheet.write('B1', 'Rs.0.0', cell_format)
worksheet.write('C1', 'Rs.0.0', cell_format)

worksheet.write('A2', 'Rs.0.0', cell_format)
worksheet.write('B2', 'Rs.0.0', cell_format)
worksheet.write('C2', 'Rs.0.0', cell_format)

workbook.close()


