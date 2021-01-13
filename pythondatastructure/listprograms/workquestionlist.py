employees=[[1001,"ajay","qa",1981,2003],
           [1002,"vijay","developer",1992,2008],
           [1003,"arun","ba",1989,2010],
           [1004,"amal","developer",2009,2014],
           [1005,"vimal","developer",1987,1989]]
#print all employee designation
for emp in employees:
    print("employees designation",emp[2])
#print all employee whose designation=designer
for emp in employees:
    if(emp[2]=="developer"):
        print("employee with designation developer",emp[1])
#print all employee whose experience is greater than 9
for emp in employees:
    total=emp[4]-emp[3]
    if(total>9):
        print("employees with experience greater than 9",emp)
#print all students who works in 1980's
start=1980
end=1989
for emp in employees:
    if(emp[3]>start):
        if(emp[4]<=end):
            print("employee in 1980's",emp[1])