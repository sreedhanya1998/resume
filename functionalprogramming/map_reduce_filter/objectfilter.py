class Employee:
    def __init__(self,name,id,salary,desig):
        self.name=name
        self.id=id
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name

obj=Employee("ajay",100,25000,"developer")
obj1=Employee("vijay",101,20000,"develop")
obj2=Employee("binoy",102,22000,"qa")
lst=[]
lst.append(obj)
lst.append(obj1)
lst.append(obj2)
for emp in lst:
   print(emp.name)
#covert to upper case
uppname=list(map(lambda emp:emp.name.upper(),lst))
print(uppname)