

class birds:
    def category(self):
        print("This is category of bird")
    def fly(self):
        print("I can fly")
class ostrich(birds):
    def fly(self):
        print("sorry, i can't fly")
class crow(birds):
    pass
class sparrow(birds):
    def size(self):
        print("I am small in size")
objsparrow=sparrow()
objcrow=crow()
objostrich=ostrich()
objsparrow.category()
objsparrow.size()
objsparrow.fly()
objostrich.fly()