f=open("complete.csv")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirmed_cases=data[8]
    if state in dict:
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
for k,v in dict.items():
    print(k,v)
#highest=max(dict,key=dict.get)
#print(highest,dict[highest])
##lowest=min(dict,key=dict.get)
#print(lowest,dict[lowest])
#sort state based on confirmed cases


