class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def getName(self):
        return self.__name    

    def getAge(self):
        return self.__age

Person1=Person("ABC",22)
 print(Person1.__name)        
print(Person1._Person__name)