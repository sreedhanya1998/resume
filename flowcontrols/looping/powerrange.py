n=int(input("enter number"))
m=int(input("enter number"))
change=n
sum=0
while(m!=0):
    sum+=change
    change=change*10+n
    m-=1
print(sum)