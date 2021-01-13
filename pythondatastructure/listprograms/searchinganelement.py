lst=[120,11,12,13,14]
num=int(input("enter the number"))
flag=0
for i in lst:
    if(num==i):
        flag=0
        break
    else:
        flag=1
if(flag==0):
    print("element present")
else:
    print("element not present")