def fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return(fact)
data=fact(3)
print(data)
data=fact(4)
print(data)