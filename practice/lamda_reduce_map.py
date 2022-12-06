from functools import reduce


# def even_nos(i):
#     return i%2==0

list1= [3,2,8,16,11,34,17]
output=list(filter(lambda i: i%2==0,list1))
print(output)
output1=list(filter(lambda i: i>15, list1))
print(output1)
#filter(lamda i: parameter, list name)


output2=list(map(lambda i: i+2,list1))
print(output2)

output3=list(map(lambda root: root**2,list1))
output3=reduce(lambda a,b:a*b,list1)
#reduce

print(output3)

#map(edits every element of collections)

