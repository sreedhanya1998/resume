from dbconnect_prgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
n=int(input("enter no.of rows"))
for i in range(n):
    values=input().split()
    sql="insert into faculty(id,name,subject) values(%s,%s,%s)"
    try:
        cursor.execute(sql,values)
        db.commit()
        print("insert correctly")
    except Exception as e:
        print(e.args)
    finally:
        db.close()