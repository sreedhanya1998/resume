#file operation read r   write w append a
#need to refernce fil
#referncename=open(filepath,modeofoperation)
f=open("names","r")
#for lines in f:
 #   print(lines)

#append to list
lst=[]
for lines in f:
    lines=lines.rstrip("\n")
    lst.append(lines)
print(lst)