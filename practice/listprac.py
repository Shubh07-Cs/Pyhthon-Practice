colors=["red", "blue", "red", "black"]
cars=["TATA", "NANO", "ALTO", "JEEP"]
#[print(x) for x in cars]
#for x in cars:
#for x in range(len(cars)):
     #print(cars[x])
newList=['AUTO']
for i in cars:
    if 'A' in i:
        newList.append(i)  
print(newList) 
null=[]
for i in colors:
    if 'e' in i:
        null.append(i)
print(null)    
nyaList=[x for x in colors if x!="red"]
print(nyaList)
nyList=[x.lower() for x in colors]
print(nyList)