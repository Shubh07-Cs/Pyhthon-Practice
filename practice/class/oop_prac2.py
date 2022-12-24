class person:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def detail(self):
        print("My name is",self.name,"and my roll no is",self.roll)


person1=person("shubh","71")
person2=person("akash","69")
person1.detail()
person2.detail()
print(id(person1))
print(id(person2))        

