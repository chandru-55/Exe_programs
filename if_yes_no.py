'''Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.'''
s = input("enter yes or no:")

if s=="Yes":
    print("yes")
elif s == "YES":
    print("yes")
elif s == "yes":
    print("yes")
else:
    print("No")
