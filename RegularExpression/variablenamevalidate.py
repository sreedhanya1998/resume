#start with a-k
#second number divisible by 3
#any no of characters
from re import*
rule='[a-kA-K][369][a-zA-Z0-9]*'
variablename=input("enter variable name")
matcher=fullmatch(rule,variablename)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")