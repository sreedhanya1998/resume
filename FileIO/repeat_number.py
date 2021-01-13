f=open("data","r")
set=set()
for lines in f:
        lines=lines.rstrip("\n")
        set.add(lines)
print(set)


