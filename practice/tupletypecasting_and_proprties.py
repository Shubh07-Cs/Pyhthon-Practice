# # tuples= stores multiple items in a single variable
# #non homogeneous
# #ordered
# #unchangable or immutable
# #allows duplicate Value
# myTuple=(1,2,3,4,4)
# print(myTuple)
# print(len(myTuple))
# tuple1=('OwO',)
# print(tuple1)
# tuple2=("car","bike","boat","jet")
# print(len(tuple2))
# print(tuple2[:3])



# #type casting
# list2=list(tuple2)
# print(list2)
# list2.insert(0,"cycle")
# print(list2)
# tuple2=tuple(list2)
# print(tuple2)
# list2=list(tuple2)
# list2.reverse()
# print(list2)
# tuple2=tuple(list2)
# print(tuple2)


# #del tuple2


# #we can put list in tuple container
# tuple7=(1,2,3,4,[5,6],7)
# print(tuple7[4][0], tuple7[5])
# tuple7[4][0]=8
# print(tuple7)


# #cancatenation and multiplication
# tuple1=(5,6,7,8)
# tuple2=(1,2,3,4)
# tuple3=tuple1+tuple2
# print(tuple3)
# tuple1.count(5)

#tuple=(10,20,30,40)
tuple=(10,20,30,40)
a=tuple[1]
b=tuple[2]
c=(a,b)
print(c)
#count and print occurence of 20
print(tuple.count(20))
print(tuple.index(40))

x=(1,)
print(type(x))


