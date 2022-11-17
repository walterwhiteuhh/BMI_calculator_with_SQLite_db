# Import modules

import sqlite3
import os.path

# Define class for users

class User:
    def __init__(self,name,height):
        self.name = name
        self.height = height

# Define class for BMI calculator & connection to SQLite database

class Bmicalculator:
    def __init__(self):
        self.datastorage={}
        if not os.path.exists('bmi.sqlte'):
            connection=sqlite3.connect('bmi.sqlte')
            cursor=connection.cursor()
            cursor.execute('''CREATE TABLE bmirechner(name TEXT, bmi REAL)''')
        else:
            connection=sqlite3.connect('bmi.sqlte')
            cursor=connection.cursor()
            cursor.execute('''SELECT name,bmi FROM bmirechner''')
            rows=cursor.fetchall()
            for row in rows:
                name=row[0]
                bmi=row[1]
                if name in self.datastorage:
                    bmis=self.datastorage[name]
                else:
                    bmis=[]
                bmis.append(bmi)
                self.datastorage.update({name:bmis})
    def calculate(self,gr,ge):
        return round(float(ge)/(float(gr)**2),2)
    def evaluate(self,b):
        if b>=25:
            return 'Übergewicht'
        elif b<18.5:
            return 'Untergewicht'
        else:
            return 'Normalgewicht'
    def add(self,n,b):
        if n in self.datastorage:
            bmis=self.datastorage[n]
        else:
            bmis=[]
        bmis.append(b)
        self.datastorage.update({n:bmis})
        connection=sqlite3.connect('bmi.sqlte')
        cursor=connection.cursor()
        cursor.execute('''INSERT INTO bmirechner VALUES(?,?)''',(n,b))
        connection.commit()
        connection.close()