f=open("emailid")
fout=open("valid_email_id","w")
email=set()
for lines in f:
    email.add(lines.rstrip("\n"))
from re import *
rule='[a-zA-Z0-9.-_][a-zA-Z0-9.-_]{5,29}@gmail.com'
for text in email:
    matcher=finditer(rule,text)
    if matcher!=None:
        fout.write(text+"\n")
    else:
        pass