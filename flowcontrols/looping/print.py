count=1
for i in range(1,13):
    print(i,end="\t")
    if(count==4):
        print()
        count=1
    else:
        count+=1
