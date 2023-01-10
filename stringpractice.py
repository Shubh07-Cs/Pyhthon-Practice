#take a user input(yourname)
Name=input("Enter your name:")
length=len(Name)
d=int(length+1)//2
print(Name[d])
#take a user input. if the lengh of string is greater than 3 characters then add "ing" as prefix else write as given.
a=input("enter a name:")
b=("ing")
character=len(a)
if character>3:
    print(a+b)
else:
    print(a) 
