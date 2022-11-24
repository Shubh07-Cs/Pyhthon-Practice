# Create a new file 
a=int(input("no1:"))
b=int(input("no2:"))
operator=input("Mathematical operator:")
if operator=="+" :
    print(a+b)
elif operator=="-" :
    print(a-b)
elif operator=="*" :
    print(a*b)
elif operator=="/" :
    print(a/b)
else:
    print("error")
