# Lists : a container which can contain any type of data. Its written inside []. Its printed by print() function.
a=[5,6,7,8,9,1]
print(a)


#List indexing
print(a[1])
#we can change an input by using list name and index no as--
a[3]=21
print(a[3])
#We can create a list with items of different types.
b=[1,"Shubh",True,7.7]
print(b)


#List slicing
Friends=["shubham", "kumar", "rai", 11, 7]
print(Friends)
print(Friends[0:4])
print(Friends[:3])


#List Methods
#(file name).sort() - updates the list in ascending order
Example=[23,47,43,32,19,99]
Example.sort()
print(Example)
#(file name).reverse() - updates the list in descending order
Example.reverse()
print(Example)
#(file name).append(_) - add new data at the end of the list
Example.append(75)
print(Example)
Example.sort()
print(Example)
#(file name).insert(_,_) This will add a new data at an index
Example.insert(5,0)#(at 5th index, put 0)
print(Example)
#(file name).pop(_) - will delete element at given index and return its value
Example.pop(5)
print(Example)
#(file name).remove(_) - wil remove given element
Example.remove(43)
print(Example)