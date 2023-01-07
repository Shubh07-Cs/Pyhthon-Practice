#if we want to change file that is immutable, we use decorators.
def division(a,b):
    print(a/b)
def new_division(func):
    def innerfunc(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return innerfunc            
div=new_division(division)
division(4,8)    