Total_no_of_classes=88
No_of_classes_attended=float(input("No_of_classes_attended="))
Percentage=(No_of_classes_attended/Total_no_of_classes)*100
print("Percentage of class attended is", Percentage)
if Percentage>75:
    print("Eligible for exam")
else:
    print("Not eligible foe exam")    
#we can also write if else as print("Eligible for exam") if Percentage>5 else print("not eligible for exam")