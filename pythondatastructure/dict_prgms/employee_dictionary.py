employees={"emp_id":120,"emp_name":"ajay","emp_desig":"developer","emp_salary":20000}
#print employee name
print(employees["emp_name"])
#check experience key is present or noy
print("emp_exp" in employees)
#add emp_exp
if("emp_exp" not in employees):
    employees["emp_exp"]=4
    print(employees)
#add 5000 to salary
employees["emp_salary"]+=5000
print(employees)
#print all key value pairs
for keys in employees:
    print(keys,employees[keys])
