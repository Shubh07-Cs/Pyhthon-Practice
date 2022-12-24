class A:
    def __init__(self):
            print("This is init of method A")#it doesnot need to be recalled
    def method1(self):
        print("This is method 1")
class B(A):        
    def method2(self):
        print("This is method2") 
    def __init__(self):
        super().__init__()#u can access both inits even after having with urself
        print("This is init of method B")
# class C(B,A):
#     def method3(self):
#         print("Aakash is my grand grand grand .............. ")       
obj1=B()
 
# obj3=C()
# obj3.method1()
# print(obj3)
