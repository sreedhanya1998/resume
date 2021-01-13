names=["a","b","c","d","e","f","g"]
passed=["a","b","c"]
name=set(names)
res=set(passed)
failed=name.difference(res)
print("failures are",failed)