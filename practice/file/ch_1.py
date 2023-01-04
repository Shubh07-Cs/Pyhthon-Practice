file_handler=open("demo.txt","r",encoding="utf-8")
#print(file_handler.read())
# print(file_handler.readline())
f1=open("demo2.txt","w")
f1.write("This is a new file\n")
f1.write("This is a random text\n")
for i in file_handler:
    f1.write(i)

# file_handler2=open("demo2.txt","w")
# print(file_handler2.write("This is my file2"))
file_handler3=open("demo3.txt","w")
print(file_handler3.write("My name is Shubham Rai.\nI'm good.Comment ca va?"))


file_handler4=open("demo3.txt","a")


# close file with f.close()


# try:
#     f=open("demo.txt")
#     #your code goes here
# finally:
#     f.close()
# #(This way we are making sure that file is closed properly even if exception is raised that cause the program file to stop.)         


# with open("demo.txt") as f:
#     f.read() # --> example
#     #your code goes here

print(file_handler.tell())
print(file_handler.seek(5))