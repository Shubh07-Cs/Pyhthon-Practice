list1=[10,20,30,40,50]
# triple all the elements in the list.
output=list(map(lambda i: i*3,list1 ))
print(output)


list2=[34,88,30,22,10,15,18]
#print out all the multiples of 5 using filter and lamda.
output2=list(filter(lambda i: i%5==0,list2))
print(output2)