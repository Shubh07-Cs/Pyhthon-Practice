class person:
    def __init__(self):
        self.name="shubham"
        self.age=18

    def update_name(self,name):
        self.name=name


    

    def compareage(self,other):
        if (self.age==other.age): 
            return True
        else:
            return False       

person1=person()
person2=person()
person1.age=22
# person1.update_name(name="atul")
# print(person1.name)
# print(person2.name)       

if person1.compareage(person2):
    print("They are of same age")
else:
    print("They are of different age")    
