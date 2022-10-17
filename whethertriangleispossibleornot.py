from email.errors import FirstHeaderLineIsContinuationDefect

Firstside=int(input("no1:")) 
Secondside=int(input("no2:"))
Thirdside=int(input("no3:"))
if Firstside+Secondside>Thirdside:
    print("True")
elif Firstside+Thirdside>Secondside:
    print("True")
elif Secondside+Thirdside>Firstside:
    print("True")
else:
    print("False")
