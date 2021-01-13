from re import *
#pattern="a+" #check for a and more than a
#pattern="a*" # a and zero occurence of a
pattern="a?"
#pattern="^a" # check for starting with a
#pattern="a$"
# pattern="a{2,3}" #check minimum 2 and maximum 3
matcher=finditer(pattern,"aaaabaabaaaaa")
for match in matcher:
    print(match.start())
    print(match.group())
######################################################################################
# matcher=fullmatch(pattern,"baaabaabaaaaabab")
# if matcher!=None:
#     print("string ending with a")
# else:
#     print("string not ending with a")
