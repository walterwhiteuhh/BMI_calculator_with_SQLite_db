import sqlite3

con = sqlite3.connect("bmi.sqlte")
curser=con.cursor()
curser.execute('''CREATE TABLE bmirechner(name TEXT, bmi REAL)''')
curser.execute('''INSERT INTO bmirechner VALUES('Tim', 22.23)''')
curser.execute('''INSERT INTO bmirechner VALUES('Alex', 22.13)''')
curser.execute('''SELECT name,bmi FROM bmirechner''')
con.commit()
rows=curser.fetchall()
print(rows)
con.close()
