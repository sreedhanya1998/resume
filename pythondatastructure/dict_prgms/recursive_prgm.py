pattern="ABABAC"
dict={}
for char in pattern:
    if(char not in dict):
        dict[char]=1
    else:
        print("recursive character",char)
        break
