text="hello hai hai hello hai"
words= text.split(" ")
#dic{}
#{"hello:1 } dict[hello]=1  #if hello not in dict
#dict[hello]+=1      if hello in dict
dict={}
for txt in words:
    if(txt not in dict):
        dict[txt]=1
    else:
        dict[txt]+=1
print(dict)



