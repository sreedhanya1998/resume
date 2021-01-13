import re
matcher=re.finditer("ab","ababababaaabbaba")
#                         0123456789
cnt=0
for match in matcher:
    print(match.start())
    cnt+=1
print("count of ab", cnt)
