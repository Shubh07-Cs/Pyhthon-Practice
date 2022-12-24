# a="Hello"
# b=[1,2,3,4,5,6]
# print(len(b))


# def add(a,b,c=0):
#     return a+b+c
# print(add(1,2,-3))#(overloading)
# print(add(4,3))    


class rectangle:
    def area(self,a=None,b=None):
        if a!=None and b!=None:
            return(a*b)
        elif a!=None:
            return (a*a)  
area1=rectangle()
print(area1.area(2,3))
print(area1.area(3))              
