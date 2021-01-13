lst=[1,2,3,5,6,7,8,8,10,11,12,15]
#    low......mid..........upp
#lower=1 upp=11
#find mid=4
#elemt=10   10>4
#low=low+1
#element<mid
#upp=upp-1
#if element==lst[mid]
 #   element found
lst.sort()
element=int(input("enter the number"))
low=0
upp=len(lst)-1
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")


