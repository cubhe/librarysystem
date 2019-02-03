from stu import stu
from stu import login
from stu import changepass
from stu import changepass
import os.path
import xlwt
import xlrd
import string
from xlutils.copy import copy
#初始学生名单
if os.path.exists('heka.xls')==False :
    testbook=xlwt.Workbook();
    worksheet=testbook.add_sheet('kaka');
    worksheet.write(0,0,'ID');
    worksheet.write(0,1,'name');
    worksheet.write(0,2,'password');
    testbook.save('heka.xls');#xlsx or xls
#初始书籍名单
if os.path.exists('books.xls')==False :
    testbook=xlwt.Workbook();
    worksheet=testbook.add_sheet('kaka');
    worksheet.write(0,0,'ID');
    worksheet.write(0,1,'bookname');
    worksheet.write(0,2,'author');
    worksheet.write(0,3,'category');
    worksheet.write(0,4,'price');
    worksheet.write(0,5,'desc');
    worksheet.write(0,6,'pubulish_data');
    testbook.save('books.xls');#xlsx or xls

#main

flag1=True;flag2=True;flag3=True;
while(flag1):
    while(flag2):
        print('**********welcome to LibrarySystem**********');
        print('1:login       2:regist        3:changepass');
        choose=int(input('input you choose:'));
        if choose==1:
            newname=input('name:  ');
            newpassword=input('password:   ');
            if  login(newname,newpassword):
                flag2=0;
        elif choose==2:
            newstu=stu();
            newstu.name=input('name:  ');
            newstu.password=int(input('password:   '));
            newstu.writedata();
            flag2=0;
        elif choose==3:
            print('请先登录:');
            name=input('name:  ');
            password=input('password:   ');
            if  login(name,password)==False:
                print('重新登录');
                continue;
            newpassword=input('输入新密码:    ');
            if changepass(name,newpassword):
               flag2=0;
        else:
            print('啥子啊');
        os.system("cls");


    while(flag3):
        print("******well come to Book Mannage Center******")
        print('操作1234567');
        choose=input('选择操作：')


        break;



#两种初始化(登录)方法
#stu0=stu('a','a');
#stu0.dispaly();
#stu0.writedata();

#修改内容
#print('');
#filename='heka.xls';
#testbook=xlrd.open_workbook(filename,formatting_info=True);
#sheet=testbook.sheet_by_index(0);
#rowNum=sheet.nrows;
#colNum=sheet.ncols;
#newbook=copy(testbook);
#sh=newbook.get_sheet(0);
##sh.write(5,0,'gu');
##sh.write(5,1,'gua')
#temp=sh.cell(rowx=5,colx=0);
#print(temp);
#newbook.save('heka.xls');

#changepass('gu','guagua');





