class Parent:
    def phone(self):
        print("have nokia")
class Child(Parent):
    def phone(self):
        print("have iphone")
c=Child()
c.phone()