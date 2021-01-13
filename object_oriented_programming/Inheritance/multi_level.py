class Parent:
    def m1(self):
        print("inside parent class")
class Child(Parent):
    def m2(self):
        print("inside child class")
class Subchild(Child):
    def m3(self):
        print("inside subchild")
sb=Subchild()
sb.m2()
