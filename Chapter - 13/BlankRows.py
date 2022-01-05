import openpyxl
r=int(input("Enter the row number: "))
n=int(input("Enter the number of blank rows to be entered : "))
file=input("Enter the file name with appropriate extension : ")
sht=input("Enter the sheet name : ")
wb=openpyxl.load_workbook(file)
sheet=wb[sht]
sheet.insert_rows(r,amount=n)
wb.save('BlankRows.xlsx')
print("Done")
