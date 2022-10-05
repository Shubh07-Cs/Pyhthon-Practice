#write a program to find square root of a number
p=input("Enter a no.")
p=int(p)
q=p**0.5
print("Square root of the no is", q)
#find area of a triangle
a=input("First side of triangle:")
b=input("Second side of triangle:")
c=input("Third side of triangle:")
a=int(a)
b=int(b)
c=int(c)
s=(a+b+c)/2
t=s*(s-a)*(s-b)*(s-c)
r=t**0.5
print("Area of the triangle is", r)