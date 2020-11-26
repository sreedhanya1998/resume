lst=[6,6,8,9,4,2,3]
out=[]
for num in lst:
    if(num>5):
        out.append((num+1))
    else:
        out.append((num-1))
print(out)