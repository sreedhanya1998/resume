bdate=input("enter bdate dd-mm-yyyy")
cdate=input("enter cdate dd-mm-yyyy")
print(bdate)
print(cdate)
bdate,bmonth,byear=bdate.split("-")
cdate,cmonth,cyear=cdate.split("-")
age=int(cyear)-int(byear)
print(age)
if(cmonth<=bmonth):
    if(cdate<bdate):
        age-=1
print("you are",age,"years old")
