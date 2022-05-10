from django.conf import settings
from django.db import models
from django.db import connection
import sys
class DBConnection:

    def __init__(self):
        try:
            print("connecting...")
            #self.db_connection = mysql.connector.connect(user='root', password='', host='localhost',
            self.db_connection = connection
            print("connect to database")
            print("database")
        except:
            print("Oops!", sys.exc_info()[0], "occured.")
            print("Cant connect to database")

    def getsingle(self, query,values=None):
         
        self.cursor = self.db_connection.cursor()
        if values == None :
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, values) 
        rows =  self.cursor.fetchone()
        return rows
    def manipulate(self, query, values):
        print(values)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute(query, values)
        self.db_connection.commit()

    def gettable(self, query,values=None):
        print(values)
        self.cursor = self.db_connection.cursor()
        if values == None :
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, values)
        columns = [col[0] for col in self.cursor.description]
        rows = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        return rows
    def isAlreadyExist(self,query,values):
        self.cursor = self.db_connection.cursor()
        if values == None :
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, values)
        columns = [col[0] for col in self.cursor.description]
        rows = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        if len(rows)>0 :
            return 1
        else:
            return 0
ob= DBConnection();
