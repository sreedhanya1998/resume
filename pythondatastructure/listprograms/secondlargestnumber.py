lst=[10,9,8,11,12,5,6]
temp=0
for i in range(0,len(lst)):
    for j in range((i+1),len(lst)):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst[1])
