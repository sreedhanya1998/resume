no1=int(input("enter no1"))
no2=int(input("enter no2"))
try:
    res=no1/no2
    print(res)
except:
    no2=int(input("enter new value for no2"))
    res = no1 / no2
    print(res)
finally:
    print("i have one database")
