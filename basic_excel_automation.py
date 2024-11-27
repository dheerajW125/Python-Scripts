from openpyxl import Workbook
from win32com.client import Dispatch

workbook = Workbook()
sheet = workbook.active

sheet["A1"]= "hello"
sheet["B1"]= "python"

workbook.save(filename="Book3.xlsx")
cell = sheet["A1"]
cell.value = "greetings"
print(cell.value)
workbook.save(filename="Book3.xlsx")

x1 = Dispatch("Excel.Application")
x1.Visible = True

wb = x1.Workbooks.Open(r'F:\Projects\Python Scripts\Book3.xlsx')
print("successful")
