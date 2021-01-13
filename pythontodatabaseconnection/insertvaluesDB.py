from dbconnect_prgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql="insert into faculty(id,name,subject) values('101','vijay','python')"
try:
    cursor.execute(sql)
    db.commit()
    print("insert correctly")
except Exception as e:
    print(e.args)
finally:
    db.close()