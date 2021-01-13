import mysql.connector
from dbconnect_prgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql="create table faculty(id varchar(20),name varchar(50),subject varchar(50))"
try:
    cursor.execute(sql)
    print("table success")
except Exception as e:
    print(e.args)
finally:
    db.close()