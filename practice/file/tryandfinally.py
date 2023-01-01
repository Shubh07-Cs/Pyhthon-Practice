# try:
#     #this block of code will run and throw errors if therevare any

# except:
#     #this will raise the errors

# else:
#     #this will execute if there are not errors

# finally:
#     #this will execute regardless the result of try and except


try:
    f=open("demo3.txt")
    try:
        f.write("ABC")
    except:
        print("Error in file")
    finally:
        f.close()
except:
                    
