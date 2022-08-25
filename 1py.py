import mysql 


mysql = pymysql.connect(host='localhost',user='root',password='200406',port=3306,database='book')
        cursor = mysql.cursor()
        cursor.execute("select * from book")
        all = cursor.fetchall()
        cursor.close()
        mysql.close()