a=int(input())
if  a%2==0:
    if 2<=a<=5:
       print("Not Weird")   
    elif 6<=a<=20 and a%2==0:
        print("Weird")
    elif 20<a and a%2==0:
        print("Not Weird")  
else:     
    print("oWeird")
    