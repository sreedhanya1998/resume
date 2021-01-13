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
for k, v in dict.items():
    highest=max(dict,key=dict.get)
    lowest=min(dict,key=dict.get)
print(highest,dict[highest])
print(lowest,dict[lowest])

