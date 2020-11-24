low=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
evensum=0
oddsum=0
for i in range(low,upper):
    if(i%2==0):
        evensum+=i
    else:
        oddsum+=i
print("oddsum",oddsum,"evensum",evensum)