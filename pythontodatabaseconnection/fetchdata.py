from dbconnect_prgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql="select * from faculty"
try:
    cursor.execute(sql)
    queryset=cursor.fetchall()
    for faculty in queryset:
        print("id=",faculty[0])
        print("name=",faculty[1])
except Exception as e:
    print(e.args)
finally:
    db.close()