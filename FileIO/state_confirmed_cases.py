f=open("complete.csv")
dict={}
for data in f:
    word=data.rstrip("\n").split(",")
    state=word[3]
    confirmed=word[8]
    if state in dict:
        dict[state]=confirmed
    else:
        dict[state]=confirmed
for k,v in dict.items():
    print(k,v)