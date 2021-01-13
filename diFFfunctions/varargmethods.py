def add(*args):
    total=0
    for num in args:
      total+=num
    print(total)

add(10,20)
add(10,20,30)

def printEmp(**args):
    print(args)

printEmp(name="ajay",birthplace="kakkkanad")