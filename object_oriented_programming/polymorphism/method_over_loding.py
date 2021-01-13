class Maths:
    def add(self):
        print("inside no ar add method")
    def add(self,num1):
        print("inside single arg add method")
    def add(self,num1,num2):
        print("inside two arg add method")
m=Maths()
m.add(10,20)
m.add(10)  #only allowing recently implemented function