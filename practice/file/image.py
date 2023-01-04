# r=open("lunch3.jpg","rb")
# print(r.read())
# r1=open("breakfast3.jpg","rb")
# for i in r:
#     r1.write(i)  
 
 
  
import os
if os.path.exists("demo.txt"):
    os.remove("demo5.txt")
else:
    print("File doesn't exist")