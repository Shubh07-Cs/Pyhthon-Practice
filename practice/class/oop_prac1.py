class laptop:

    def __init__(self,name,processor):
        self.name=name
        self.processor=processor






    def printoutput(self):
        # print("Asus","i7","1TB")
        print("My laptop name is",self.name,"and the processor is",self.processor)

laptop1=laptop("Asus","i7")        
laptop2=laptop("HP","i9")

print(id(laptop1))
print(id(laptop2))

laptop1.printoutput()
laptop2.printoutput()

