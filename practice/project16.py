

from datetime import date
byear=int(input("YoB"))
bmonth=int(input("MoB"))
bday=int(input("DoB"))
d1=date(byear, bmonth, bday)
print(d1)
cyear=int(input("CY"))
cmonth=int(input("CM"))
cday=int(input("CD"))
d2=date(cyear, cmonth, cday)
print(d2)
delta=d2-d1
print(delta.days,"DAYS")