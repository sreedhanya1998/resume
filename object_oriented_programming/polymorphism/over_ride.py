class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return str(self.age)
p=Person(25,"person1")
print(p)