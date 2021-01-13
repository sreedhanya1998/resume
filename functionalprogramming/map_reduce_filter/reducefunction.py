from functools import *
lst=[10,11,12,13,14]
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)
#minimum element
min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)
#maximum element
max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)

#sum of even numbers
sum=reduce(lambda no1,no2:no1+no2,list(filter(lambda no:no%2==0,lst)))
print(sum)
#print minimum even number
evenmin=reduce(lambda no1,no2:no1 if no1<no2 else no2,
                    list(filter(lambda no:no%2==0,lst)))
print(evenmin)