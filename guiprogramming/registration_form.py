from tkinter import *
import mysql.connector
from tkinter import messagebox
root=Tk()
from dbconnect_prgm.dbconnect import get_connection
def db_connect(username,password):
    db = get_connection()
    cursor = db.cursor()
    try:
        # sql="create table user_form(uname varchar(20),course varchar(20),semester varchar(20),form_num varchar(20))"
        # cursor.execute(sql)
        cursor.execute(("select * from user_form where username=%s AND password=%s"),(username,password))
        users=cursor.fetchone()
        return users
        # sql1="insert into user_form(uname,course,semester,form_num)values('vijay','python','4','234')"
        # cursor.execute(sql1)
        # db.commit()
        # sql2 = "insert into user_form(uname,course,semester,form_num)values('abhi','mca','2','101')"
        # cursor.execute(sql2)
        # db.commit()
    except Exception as e:
        print(e.args)
def authenticate_user():
    # uname=uentry.get()
    # course=centry.get()
    # semester=sentry.get()
    # form_num=fentry.get()
    user=userentry.get()
    passw=passentry.get()
    users=db_connect(user,passw)
    if(users==None):
        messagebox.showerror("invalid message", "error")

    else:
        messagebox.showinfo("suceesfully logged", "success")



root.title("registration form")
uname=Label(root,text="name")
ucourse=Label(root,text="course")
semester=Label(root,text="semester")
form_num=Label(root,text="form_number")
username=Label(root,text="username")
password=Label(root,text="password")
uentry=Entry(root)
centry=Entry(root)
sentry=Entry(root)
fentry=Entry(root)
userentry=Entry(root)
passentry=Entry(root)
btn=Button(root,text="submit",command=authenticate_user)
uname.grid(row=0,column=0)
ucourse.grid(row=1,column=0)
semester.grid(row=2,column=0)
form_num.grid(row=3,column=0)
username.grid(row=4,column=0)
password.grid(row=5,column=0)
uentry.grid(row=0,column=1)
centry.grid(row=1,column=1)
sentry.grid(row=2,column=1)
fentry.grid(row=3,column=1)
userentry.grid(row=4,column=1)
passentry.grid(row=5,column=1)
btn.grid(row=6,column=1)

root.mainloop()
