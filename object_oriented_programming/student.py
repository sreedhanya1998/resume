class Student:
    def set_student(self,roll,name,course,total):
        self.roll=roll
        self.course=course
        self.total=total
        self.name=name
    def print_student(self):
        print("roll",self.roll)
        print("course", self.course)
        print("total", self.total)
        print("name", self.name)
obj=Student()
obj.set_student(10,"ajay","bca",150)
obj.print_student()
obj1=Student()
obj1.set_student(20,"vijay","mca",200)
obj1.print_student()