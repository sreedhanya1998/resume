# lst=[10,11,12,13,14]
# #print even number
# even=list(filter(lambda no:no%2==0,lst))
# print(even)
name=["ajay","aji","binoy","abhi","anu"]
#convert all name to uppercase
upp=list(map(lambda name:name.upper(),name))
print(upp)
#select name starting with a
aname=list(filter(lambda name:name[0]=='a',name))
print(aname)