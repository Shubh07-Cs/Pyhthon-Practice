class student:

    def __init__(self,marks1,marks2,marks3):
        self.web=marks1
        self.python=marks2
        self.maths=marks3

    def average(self):
        print((self.web+self.python+self.maths)/3)#perform the parameter here

    def low(self):
        a=[self.web,self.python,self.maths]
        print(min(a))

    def classmethodexample(cls):   
        return cls.numberofsubject

    def staticmethodexample():
        print("This is an example of static method")

    # def getmarks(self):
    #     return self.maths #Accessors

    # def setmarks(self,marks):
    #     self.maths=marks   #Mutators       

student1=student(5,4,3)        
student2=student(7,8,9)        
aakash=student(1,6,0)
student1.average()# and just call def here

aakash.low()


