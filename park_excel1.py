import xlsxwriter

workbook = xlsxwriter.Workbook('park1.xlsx')
worksheet = workbook.add_worksheet("My sheet")

cell_format = workbook.add_format({'font_color': 'black'})
cell_format.set_align('center')

worksheet.write('A1', '1', cell_format)
worksheet.write('B1', '2', cell_format)
worksheet.write('C1', '3', cell_format)

worksheet.write('A2', '4', cell_format)
worksheet.write('B2', '5', cell_format)
worksheet.write('C2', '6', cell_format)



workbook.close()


