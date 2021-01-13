f=open("student","r")
f1=open("passed","r")
#st=set()
#set=set()
#for lines in f:
 #   lines=lines.rstrip("\n")
  #  st.add(lines)
#for lines in f1:
 #   lines = lines.rstrip("\n")
  #  set.add(lines)
#failed=st.difference(set)
#print("failed students are:",failed)

def convert_to_set(file):
    file_set=set()
    for names in f:
        file_set.add(names.rstrip("\n"))
    return file_set
student_set=convert_to_set(f)
student_passed=convert_to_set(f1)
print(student_set-student_passed)



