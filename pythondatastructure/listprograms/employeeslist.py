employees=[[100,"ajay","qa",25000],
          [101,"vijay","developer",25000],
          [102,"amal","ba",20000],
          [103,"saaaa","qa",25000]]

#print all employee id
for employee in employees:
    print(employee[0])
for employee in employees:
    if(employee[2]=="developer"):
        print(employee)


totalsalary=0
totalba=0
totalqa=0
for employee in employees:
    if(employee[2]=="developer"):
        totalsalary+=employee[3]

    elif(employee[2]=="qa"):
        totalqa+=employee[3]

    elif(employee[2]=="ba"):
        totalba+=employee[3]


print("developer salary", totalsalary)
print("qa salary", totalqa)
print("ba salary", totalba)
