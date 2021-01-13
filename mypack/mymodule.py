def div_dec(func):
    def wrap(no1,no2):
        if(no1<no2):
            no1,no2=no2,no1
        return func(no1,no2)
    return wrap




@div_dec
def div(num1,num2):
    return num1/num2

data=div(5,10)
print(data)