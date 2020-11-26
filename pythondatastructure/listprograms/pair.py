lst=[1,2,3,4,5,6,7]   #value=6 print(4,2)
for i in lst:
    for j in lst:
        total=i+j
        if(total==6):
            print((i,j))
            break
