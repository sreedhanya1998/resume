low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
sum=0
if(low>upp):
    print("error")
while(low<=upp):
    if(low%2!=0):
        sum+=low
    low+=1
print(sum)