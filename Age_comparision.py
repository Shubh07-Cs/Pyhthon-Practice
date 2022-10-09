# Take input of age from 3 people 
#Determine the oldest and youngest
Age_of_first_guy=float(input("Age of first guy"))
Age_of_second_guy=float(input("Age of second guy"))
Age_of_third_guy=float(input("Age of third guy"))
if Age_of_first_guy>Age_of_second_guy and Age_of_first_guy>Age_of_third_guy:
    print("First guy is oldest")
elif Age_of_second_guy>Age_of_first_guy and Age_of_second_guy>Age_of_third_guy:
    print("Second guy is oldest")
elif Age_of_third_guy>Age_of_first_guy and Age_of_third_guy>Age_of_second_guy:
    print("Third is oldest")
if Age_of_first_guy<Age_of_second_guy and Age_of_first_guy<Age_of_third_guy:
    print("First guy is youngest")
elif Age_of_second_guy<Age_of_first_guy and Age_of_second_guy<Age_of_third_guy:
    print("Second guy is youngest")
elif Age_of_third_guy<Age_of_first_guy and Age_of_third_guy<Age_of_second_guy:
    print("Third is youngest")
else:
    print("All guy of same age") 