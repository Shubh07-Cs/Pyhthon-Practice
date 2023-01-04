                                                                #SETS

                                                    
#set - stores multiple values in single variable
#sets are unordered
#sets written in {}
#sets are unchangable/immutable  (NOTE: YOU CAN ADD SOMETHING IN SET BUT YOU CANnot REPEAT AN INPUT)
#duplicates not allowed
#non homogeneous
# myset={10,"ram"}
# print(myset)
myset={"cpu","ram","rom"}
if "rom" in myset:
    print("rom")
# myset1={"cpu"}
# print(type(myset1))
tuple1=("H","E","L","L","O")
(a,b,c,d,e)=tuple1
print(a+b+c+d+e)


a={1,2,"ram"}

#         myset.add
#         myset1.update(myset2)
#         myset1.remove(myset2)
#         myset1.discard(myset2)
#         myset1.pop(myset2)
#         myset1.union(myset2)
#         myset1.intersection(myset2)
#         myset1.symmetric_difference(myset2)
#         del
myset.union(a)

print(myset)


