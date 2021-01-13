f=open("complete.csv")
dict={}

for lines in f:
    word = lines.rstrip("\n").split(",")
    state = word[3]
    confirmed = word[8]
    if state in dict:
        dict[state] = int(confirmed)
    else:
        dict[state] = int(confirmed)
srt=sorted(dict,key=dict.get,reverse=True)
print("sorted",srt)