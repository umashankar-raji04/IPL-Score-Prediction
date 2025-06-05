import openpyxl as xlsx
wb = xlsx.load_workbook_part('ipl.xlsx')
sheet = wb['Rohit']
#cell= sheet['A1']
cell=sheet.cell(1,1)
print(cell)