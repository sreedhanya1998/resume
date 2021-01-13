students=[[100,"ajay","mca",200],[101,"vijay","bca",201],[102,"amal","mca",777]]
#print all student name
for student in students:
    print(student[1])
#print students rollnumber
for student in students:
    print(student[0])
#print student with course mca
for student in students:
    if(student[2]=="mca"):
        print(student)
#print student total>100
#find total sum of student total  group by course

totalmca=0
totalbca=0
for student in students:
    if(student[2]=="mca"):
        totalmca+=student[3]
    elif(student[2]=="bca"):
        totalbca+=student[3]
print("total mca student",totalmca)
print("total bca student",totalbca)