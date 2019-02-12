#建立试图用户对象实现注册功能
#通过xlwt与xlrd查表实现登录和修改密码功能
import xlwt
import xlrd
import string
from xlutils.copy import copy
class stu:
    def __init__(self,name=None,password=None):
        self.name=name;
        self.password=password;
    def regist(self,name=None,password=None):
        self.name=name;
        self.password=password;
        return True;
    def dispaly(self):
        print(self.name,self.password);
    def writedata(self):
        filename='heka.xls';
        testbook=xlrd.open_workbook(filename,formatting_info=True);
        sheet=testbook.sheet_by_index(0);
        rowNum=sheet.nrows;
        colNum=sheet.ncols;
        newbook=copy(testbook);
        newsheet=newbook.get_sheet(0);
        newsheet.write(rowNum,0,rowNum);
        newsheet.write(rowNum,1,self.name);
        newsheet.write(rowNum,2,self.password)
        newbook.save('heka.xls');
        return True;


def login(name,password):
    filename='heka.xls';
    testbook=xlrd.open_workbook(filename,formatting_info=True);
    sheet=testbook.sheet_by_index(0);
    rowNum=sheet.nrows;
    colNum=sheet.ncols;
    print(rowNum,colNum);
    newbook=copy(testbook);
    newsheet=newbook.get_sheet(0);
    for i in range(1,rowNum):
        tempname=sheet.cell(i,1).value;
        temppass=sheet.cell(i,2).value;
        temppass=int(temppass);
        password=int(password);
        #print(tempname,'  ',temppass);
        #print(name,'  ',password);
        if( name== tempname ):
            print('get it ');
            if(password==temppass):
                print('登陆成功');
                newbook.save('heka.xls');
                return True;
            else:
                print('密码错误');
                return False;
        if(i==rowNum):
            print('failed');
    
    return False;

def changepass(name,password):
    filename='heka.xls';
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
            print('修改成功');
            print('get it ');
            newsheet.write(i,2,password);
            break;
    newbook.save('heka.xls');
    return True;


