a= "Ram"#(length=3 whose counting starts from 0, So here R syntax has 0 , a has 1 and m has 2 face value)
b= " aam khata hai."
c=a + b#(Concatenating two strings)
print(c)

#String slicing
print(a[0])
print(a[1])
print(a[2])
# a is name of the variable containing that string
# We cant change letter like we do in integer
# like a[1]=j --> this is not gonna work
#if we want to show more than one letter in one line,then-
print(a[0:2])
print(a[0:3])
print(a[1:3])
print(a[1:2])
# Start counting from 0 and accordingly find position of letter u want to print(starting from begining and excluding last is called string slicing)
# use negative index- if we want to know a letter from last and we dont know its face value, we can use negative index to print it. For example -
print(a[-1])
#Note
print(a[:3])
print(a[0:])
#slicing with skip value
d="ShubhamIsAGoodBoy"
print(d[:9])
print(d[0:18:1])
print(d[0:18:2])
print(d[1:15:3])#(the no after : decides which positioned no is to be skipped, so if we write 3 it will skip 2 continuous nos)

## String functions
story="There is a guy named Shubham. He is trying to learn python and french since french toasts are very tasty. Didn't get logic ?? I'm not here to tell you a story. This is just a junk. "
print(len(story))#len defines no of lengths in the string
print(story.endswith("junk"))
print(story.count("is"))#used to count no of letters 
print(story.capitalize())#capitalize first letter of string and all others small
print(story.find("shubham"))#finds the word and returns the index of first occurence of that word in that string
print(story.find("Shubham"))
print(story.replace("Shubham","Shubh07"))# replace old word with new word in entire string.