#Write a pyhton program to display a user entered name followed by Good Afternoon using input() function
#/n to write input in new line
a=input("Enter Your Name:")
b="Good Morning "
print(b + a)
# Write a program to fill in a letter template given below with name and date.***(important)
c=letter='''Dear <|Name|>
you are selected!

Date: <|Date|>'''
Name=input("Enter your name\n")
Date=input("Enter Date\n")
letter=letter.replace("<|Name|>", Name)
letter=letter.replace("<|Date|>", Date)
print(letter)  
#write a program to detect double spaces in a string.
story="There is a guy named Shubham. He is trying to learn  python and french since  french toasts are very tasty. Didn't get logic ?? I'm not here to tell you a story. This is just a junk. " 
d=story.find("There") 
print(d)             
#Replace the double spaces from problem 3 with single spaces.
e=story.replace("  "," ") 
print(e)
#Writ a program to format the following kahaani using escape sequence characters.
#kahaani="Dear Shubhi, This python practice is tiring. Ahh....!"
kahaani="Dear Shubhi, This python practice is tiring. Ahh....!"
fancy_kahaani="Dear Shubhi,\n\t This python practice is tiring.\n\t\t\t\t\t Ahh....!"
#\n is used to break line and \t is used to give a space equals to tab
print(fancy_kahaani)
