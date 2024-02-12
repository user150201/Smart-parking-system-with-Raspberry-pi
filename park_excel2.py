import xlsxwriter

workbook = xlsxwriter.Workbook('park2.xlsx')
worksheet = workbook.add_worksheet("My sheet")

cell_format = workbook.add_format({'font_color': 'black'})
cell_format.set_align('center')

worksheet.write('A1', '00:00:00', cell_format)
worksheet.write('B1', '00:00:00', cell_format)
worksheet.write('C1', '00:00:00', cell_format)

worksheet.write('A2', '00:00:00', cell_format)
worksheet.write('B2', '00:00:00', cell_format)
worksheet.write('C2', '00:00:00', cell_format)


workbook.close()


