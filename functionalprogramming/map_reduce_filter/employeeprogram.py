from functools import *
class Employee:
    def __init__(self,eid,ename,desig,sal,exp):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def __str__(self):
        return self.ename

f=open("new_data","r")
employee_list=[]
for lines in f:
    eid,ename,desig,sal,exp=lines.rstrip("\n").split(",")
    employee_list.append(Employee(eid,ename,desig,sal,exp))
#highest salary
highest_salary=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                      list(map(lambda emp:emp.sal,employee_list)))
print(highest_salary)
#highest salary employee details
sal_detail=list(map(lambda emp:emp.ename,employee_list))
highest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,sal_detail)
print(highest)
#find highest salary whose designation is developer
desigdevelop=list(filter(lambda emp:emp.desig=="developer",employee_list))
salary=list(map(lambda emp:emp.sal,desigdevelop))
emp_details=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salary)
print(emp_details)

