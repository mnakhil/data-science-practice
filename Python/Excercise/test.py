import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="133101@mys0l")
my_cursor=mydb.cursor()
my_cursor.execute("CREATE DATABASE test1")
