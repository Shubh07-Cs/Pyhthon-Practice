#if we want to change file that is immutable, we use decorators.
def div(a,b):
    print(a/b)
def new_div(func):
    def innerfunc(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return innerfunc            
div=new_div(div)
div(4,8)    