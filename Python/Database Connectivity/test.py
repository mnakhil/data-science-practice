import mysql.connector
class connect:
    def __init__(self):
        mydb=mysql.connector.connect(host="localhost",user="root",password="133101@mys0l")
        self.my_cursor=mydb.cursor()
        #my_cursor.execute()
        self.my_cursor.execute("CREATE DATABASE fundb")
    def create_table(self):
    {
        self.my_cursor.execute("CREATE TABLE newtable(Name char(10))")
    }
class main:
    conn=connect()

    

