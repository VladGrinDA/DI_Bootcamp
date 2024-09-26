import openpyxl

wb = openpyxl.load_workbook('ex2_Plants.xlsx')

ws = wb.active

print('The following plants are not in stock:')

plant_name = ws['A2']
i = 0
while True:
    if plant_name.value is None:
       break
    
    if i > 1e5:
        raise Exception('Infinite loop detected')
    
    if plant_name.offset(0, 7).value == 'No':
        print(plant_name.value)

    plant_name = plant_name.offset(1, 0)
    i += 1

wb.close()
