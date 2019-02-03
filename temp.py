
import xlrd
book=xlrd.open_workbook("heka.xls");
shit=book.sheet_by_index(0);
for i in range(1,10):
    temp=shit.cell(i,0).value;
    print(temp);

