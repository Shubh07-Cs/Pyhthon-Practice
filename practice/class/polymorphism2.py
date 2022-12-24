class vehicle:
    def seat(self):
        print("4 seater")
class car1(vehicle):
    pass
class car2(vehicle):
    pass
class truck(vehicle):
    def seat(self):
        print("20 seater")
carbmw=car1()
carmg=car2()
trucku=truck()        
carbmw.seat()
trucku.seat()