class Parent:
    def phone(self):
        print("have phone")
    def __lap_top(self): #private method
        print("have laptop")
class Child(Parent):
    pass
ch=Child()
ch.phone()