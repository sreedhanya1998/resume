from re import *
###########################predefined character set##############################
#pattern='[a-x]'
#pattern='[0-9]'
#pattern='[^0-9]' #except numbers
#pattern='[^a-z]' # except lower case charaxters
#pattern='[a-zA-Z]'#check both upper and lower cases
#pattern='[a-zA-Z0-9]'#except special characters
#pattern='[^ a-zA-Z0-9]'#special character
########################predefined characters###############################################
#pattern='\s' #check space
#pattern='\S' #except space
# pattern='\d'#check for digits
# pattern='\D'#except digit
# pattern='\w' #except special character
pattern='\W' #check special character
matcher=finditer(pattern,"abc Z@7k")
for match in matcher:
    print(match.start())
    print(match.group())
