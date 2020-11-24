num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("secondlargestnumber",num2)
    else:
        print("secondlargestnumber",num3)
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print("secondlargestnumber",num1)
    else:
        print("seconlargestnumber",num3)
elif((num3>num2)&(num3>num1)):
    if(num2>num1):
        print("secondlargestnumber",num2)
    else:
        print("secondlargestnumber",num1)
else:
    pass