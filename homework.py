from stu import stu
from stu import login
from stu import changepass
from stu import changepass
import books
import os.path
import xlwt
import xlrd
import string
import time
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
        elif choose==1121:
            break;
        else:
            print('啥子啊');
            time.sleep(1);
        os.system("cls");
    while(flag3):
        print("******wellcome to Book Mannage Center******")
        print('操作\n1:查询所有书籍信息\n2:通过书名查询一本书  \
                         \n3:通过价格查询书籍\n4:添加一本书\n5:删除一本书 \
                         \n6:修改一本书\n7:退出系统\n');
        choose=int(input('选择操作：'));
        if choose==1:
            books.show_all();
            print("5s后退出");
            time.sleep(5);
        elif choose==2:
            name=input('请输入名字：');
            print(name);
            books.show_by_name(name);
            time.sleep(5);
        elif choose==3:
            price=input('请输入价格：');
            print(price);
            books.show_by_price(price);
            time.sleep(5);
        elif choose==4:
            new_book=books.book();
            new_book.name=input('name:  ');
            new_book.author=input('author:   ');
            new_book.category=input('category:   ');
            new_book.price=input('price:   ');
            new_book.desc=input('desc:   ');
            new_book.writedata();
            print("test4");
        elif choose==5:
            name=input("book name：")
            books.delete_book(name);
            print("test5");
        elif choose==6:
            #修改书
            print("test6");
        elif choose==7:
            for i in range(0,3):
                print("欢迎使用图书馆系统",3-i,"秒后返回 欢迎下次再来！");
                time.sleep(1);
                if i==3:break;
            flag1=0;
            break;
        else:
            print("请正确输入");
            time.sleep(1);
        time.sleep(1);
        os.system("cls");



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