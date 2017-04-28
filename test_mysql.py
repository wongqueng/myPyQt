import MySQLdb
import mysql.connector

db=MySQLdb.Connect("localhost","root","huangqiang","myjava")

cursor=db.cursor()
# sql = "INSERT INTO EMPLOYEE(NAME,  AGE,  INCOME) \
#        VALUES ('%s', '%d',  '%d' )" % \
#        ('TOM', 22, 3000)
sql="select * from employee"
cursor.execute(sql)
# db.commit()
results = cursor.fetchall()
for row in results:
    fname = row[0]
    age = row[1]
    income = row[2]
    print "fname=%s,age=%d,income=%d" % (fname, age, income)
db.close()