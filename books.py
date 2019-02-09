import numpy as np
import xlwt
import xlrd
from xlutils.copy import copy
class book:
    def __init__(self,bookname=None,author=None,category=None,price=None,desc=None,pubulish_data=None):
        self.bookname=bookname;
        self.author=author;
        self.category=category;
        self.price=price;
        self.desc=desc;
        self.pubulish_data=pubulish_data;
    def add(self,name=None,password=None):
        self.bookname=bookname;
        self.author=author;
        self.category=category;
        self.price=price;
        self.desc=desc;
        self.pubulish_data=pubulish_data;
        return True;
    def dispaly(self):
        print(self.bookname,self.author,self.category,self.price,self.desc,self.pubulish_data);
    def writedata(self):
        filename='books.xls';
        testbook=xlrd.open_workbook(filename,formatting_info=True);
        sheet=testbook.sheet_by_index(0);
        rowNum=sheet.nrows;
        colNum=sheet.ncols;
        newbook=copy(testbook);
        newsheet=newbook.get_sheet(0);
        newsheet.write(rowNum,0,self.name);
        newsheet.write(rowNum,1,self.password)
        newbook.save('books.xls');
        return True;
    

    def changebook(self,newinfo):
        
        return True;

def show_all():
    filename='books.xls';
    testbook=xlrd.open_workbook(filename,formatting_info=True);
    sheet=testbook.sheet_by_index(0);
    rowNum=sheet.nrows;
    colNum=sheet.ncols;
    print(rowNum,colNum);
    for i in range(1,rowNum):
        temp=sheet.cell(i,1).value;
        print(temp);
    return True;
def show_by_name():
    return True;
def show_by_price():
    return True;
def delete_book():
    return True;
