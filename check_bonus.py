# A company decided to givebonus of 1000Rs to employees
#employee if his/her service is more than 5 years
#Ask user their salary and year of service and print 
#the net bonus amount
Duration_of_service=float(input("Enter DOS:"))
Salary_of_employee=float(input("Your salary:"))
bonus=1000
if Duration_of_service>5:
    print("Your Net bonus salary is", Salary_of_employee+bonus)
else:
    print(Salary_of_employee)    