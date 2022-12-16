def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def div(a,b):
    print(a/b)     
a=int(input("enter a no"))
b=int(input("enter a no"))
c=str(input("operator: "))        
if c=="+":
    add(a,b)
elif c=="-":
    sub(a,b)
elif c=="*":
    multi(a,b)
elif c=="/":
    div(a,b)               