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
    print("书名  作者  分类  价格  描述")
    for i in range(1,rowNum):
        print(sheet.cell(i,1).value,sheet.cell(i,2).value,sheet.cell(i,3).value,sheet.cell(i,4).value,sheet.cell(i,5).value);
    return True;
def show_by_name(name):
    filename='books.xls';
    testbook=xlrd.open_workbook(filename,formatting_info=True);
    sheet=testbook.sheet_by_index(0);
    rowNum=sheet.nrows;
    colNum=sheet.ncols;
    booknum=0;
    for i in range(1,rowNum):
        temp=sheet.cell(i,1).value;
        print(name,'  ',temp);
        if( name== temp ):
            print(sheet.cell(i,1).value,sheet.cell(i,2).value,sheet.cell(i,3).value,sheet.cell(i,4).value,sheet.cell(i,5).value);
            print('get it ');
            booknum+=1 ;
    print("找到",booknum,"本书");
    return True;
def show_by_price(price):
    filename='books.xls';
    testbook=xlrd.open_workbook(filename,formatting_info=True);
    sheet=testbook.sheet_by_index(0);
    rowNum=sheet.nrows;
    colNum=sheet.ncols;
    price=float(price);
    for i in range(1,rowNum):
        temp=float(sheet.cell(i,4).value);
        #print(name,'  ',temp);
        if( price== temp ):
            print(sheet.cell(i,1).value,sheet.cell(i,2).value,sheet.cell(i,3).value,sheet.cell(i,4).value,sheet.cell(i,5).value);
            #print('get it ');
            break;
    return True;
def delete_book(name):
    filename='books.xls';
    testbook=xlrd.open_workbook(filename,formatting_info=True);
    sheet=testbook.sheet_by_index(0);
    rowNum=sheet.nrows;
    colNum=sheet.ncols;
    print(rowNum,colNum);
    newbook=copy(testbook);
    newsheet=newbook.get_sheet(0);
    for i in range(1,rowNum):
        temp=sheet.cell(i,1).value;
        #print(name,'  ',temp);
        if( name== temp ):
            print('删除成功');
            print('get it ');
            newsheet.write(i,1,' ');
            newsheet.write(i,2,' ');
            newsheet.write(i,3,' ');
            newsheet.write(i,4,' ');
            break;
    newbook.save('books.xls');
    return True;
