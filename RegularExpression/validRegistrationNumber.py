#KL08BS1375=valid
#GJ08BN2211=invalid
f=open("registrationnumbers")
fout=open("valid_registration_number","w")
regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip("\n"))
from re import *

rule='KL\d{2}[A-Z]{1,2}\d{1,4}'
for vehiclenum in regnum:
    matcher=fullmatch(rule,vehiclenum)
    if matcher!=None:
        fout.write(vehiclenum+"\n")
    else:
       pass
