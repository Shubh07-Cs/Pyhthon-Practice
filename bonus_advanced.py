# Company will give bonus based on following criteria-
# Time spent in company       Bonus
# greater than 10 yrs          10%
# more than 6 yrs and less     8%
#            than 10 yrs
#less than 6 yrs               5%
#ask the salary and time spent from the user
#print the net bonus amount accordingly
salary=float(input("Your salary="))
bonus1=salary/10
bonus2=(salary*2)/25
bonus3=salary/20
service_duration=float(input("Your DOS="))
if service_duration>10:
    print(salary+bonus1)
elif service_duration>6 and service_duration<=10:
    print(salary+bonus2)    
elif service_duration<6:
    print(salary+bonus3)    
