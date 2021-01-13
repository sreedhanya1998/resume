from tkinter import *
import mysql.connector
from tkinter import messagebox
root=Tk()
from dbconnect_prgm.dbconnect import get_connection
def db_connect(usename,password):
    db=get_connection()
    cursor=db.cursor()
    try:
        cursor.execute(("select * from users where username=%s AND password=%s")%(usename,password))
        user=cursor.fetchone()
        return user
        # id="101"
        # name="test2"
        # usertest="test2"
        # userpwd="test2"
        sql="insert into users(id,name,username,password)values(%s,%s,%s,%s)"
        value=("101","test2","test2","test2")
        cursor.execute(sql,value)
        db.commit()
    except Exception as e:
        print(e.args)

def autenthicate_user():
    print("inside.....")
    uname=uentry.get()
    pname=pentry.get()
    user=db_connect(uname,pname)
    if(user==None):
        messagebox.showerror("invalid user","error")
    else:
        messagebox.showinfo("logged succesfully","success")
ulabel=Label(root,text="username")
plabel=Label(root,text="password")
uentry=Entry(root)
pentry=Entry(root)
btn=Button(root,command=autenthicate_user,text="submit")
ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)
uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)
btn.grid(row=3,column=0)
root.mainloop()
