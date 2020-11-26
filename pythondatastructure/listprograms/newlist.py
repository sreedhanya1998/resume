marks=[10,20,30,40,50]
print(marks)
marks.append(60)
print(marks)
marks[0]=100
print(marks)
marks.insert(3,90)
print(marks)
print(marks[1:5:2])
print(marks[1:6:2])
for item in marks:
    print(item)
marks.remove(90)
print(marks)