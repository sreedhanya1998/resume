from tkinter import *

root=Tk()
root.title("main")
label1=Label(root,text="username")
entry1=Entry(root)
label2=Label(root,text="emailaddress")
entry2=Entry(root)


label1.pack()
entry1.pack()
label2.pack()

entry2.pack()
root.mainloop()