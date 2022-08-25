import datetime

from django.shortcuts import render,redirect
import pymysql

# Create your views here.


list_text = []
def Web2(request):

    for i in range(5):
        list_text.append(i)

    return render(request,'book2.html',{'html':list_text})

def Web3(request):
    if request.method == "GET":
        mysql = pymysql.connect(host='localhost',user='root',password='200406',port=3306,database='books')
        cursor = mysql.cursor()
        cursor.execute("select * from books")
        all = cursor.fetchall()
        cursor.close()
        mysql.close()
        return render(request,'book3.html',{'ft':all})

    else:

        text = request.POST.get('ft')


    mysql = pymysql.connect(host='localhost',user='root',password='200406',port=3306,database='books')
    cursor = mysql.cursor()
    time = datetime.datetime.now()
    print(time)
    sql = 'insert into books(text,datetime) values("{}","{}")'.format(text,time)
    cursor.execute(sql)
    mysql.commit()
    cursor.close()
    mysql.close()
    return redirect('/book1/')

def ziyuan(request):
    return render(request,'ziyuan.html')


def login(request):
    return render(request,'login.html')
