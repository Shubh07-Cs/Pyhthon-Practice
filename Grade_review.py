# and or all
Marks=float(input("Your Marks="))
if Marks>90 and Marks<=100:
    print("Your grade is A")
elif Marks>80 and Marks<=90:
    print("Your grade is B")    
elif Marks>70 and Marks<=80:
    print("Your grade is C")
elif Marks>=0 and Marks<=70:
    print("Your grade is D")    
else:
    print("invalid marks")