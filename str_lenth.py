'''
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''
def max_len(y):
     return max(y,key=len)
x=input('enter two string with using space\n')
print(max_len(x.split()))
print(len(x))
