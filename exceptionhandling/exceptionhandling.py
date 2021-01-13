no1=int(input("enter no1"))
no2=int(input("enter no2"))
lst=[1,4,5]
try:
    res=no1/no2
    print(res)
except Exception as e:
    print(e.args)
try:
    print(lst[4])
except Exception as e:
    print(e.args)