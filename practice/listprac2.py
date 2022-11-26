number=[1,2,3,4,2,5,6]
#write a program to turn every item of list into its square
#for i in number:
#    if len(number)<=5:
#     print(i*i,end=' ')
#in the above list , find value 2, if it is present, replace it with 200,only update the first occurance.     
for i in number:
    if i==2:
     g=number.index(i)
     number.remove(i)
     number.insert(g,200)
     break
print(number)


        
#cancatenation
list1=['x','y','z']
list2=[1,2,3]
list3=list1+list2
print(list3)

list1.append(list2)
print(list1)

for x in list2:
    list1.append(x)
    print(list1)
    break