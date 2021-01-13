from re import*
f=open("phonenumbers")
fout=open("valid_phone_number","w")
phonenum=set()
for numbers in f:
    phonenum.add(numbers.rstrip("\n"))
rule='[6789]{1}[0-9]{9}'
for num in phonenum:
    matcher=fullmatch(rule,num)
    if matcher!=None:
        fout.write(num+"\n")
    else:
        pass