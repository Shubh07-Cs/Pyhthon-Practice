class car:
    wheels=4

    def __init__(self,brand,mil):
        self.brand=brand
        self.mil=mil

car1=car("Tesla","10")
car2=car("Audi","8")

print(car1.brand,car1.mil)
print(car2.brand,car2.mil)
print(car1.wheels)
print(car2.wheels)


