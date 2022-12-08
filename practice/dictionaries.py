    #dictionary

#Dictionary is used to store data values in key value pair


myDictionary={ 
    "name":"Shubham",
    "age":20,
    "class":"KOC28",
    "percentage":"101%",
    "percentage":"10%"
}

#they are ordered in nature
print(myDictionary)

#same keys overwrite value.

#they are immutable.

print(len(myDictionary))

#Duplicates are not allowed

#access any key
print(myDictionary.get("age"))

#find keys
print(myDictionary.keys())
#output is list

#find values
print(myDictionary.values())
#output is list

#write items
print(myDictionary.items())
#output is tuple.

#change values
# z=myDictionary["age"]=55
# print(z)

#change values
z = (myDictionary.update({"age":18}))
print(z)

# myDictionary.pop("percentage")
# print(myDictionary)


myDictionary1={
    "class":{
        "student":{
            "name":"abc",
            "marks":{
                "python":90,
                "web":95
            }
        }
    }
}
w=myDictionary1["class"]["student"]["marks"]["web"]
print(w)