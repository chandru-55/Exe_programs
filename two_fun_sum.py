'''
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.
'''
def sum(s1,s2):
    s3 = s1 + s2
    print("the sum of the value:", s3)

def main():
    s1 = int(input("enter the s1 value:"))
    s2 = int(input("enter the s2 value:"))
    sum(s1,s2)
if __name__=="__main__":
    main()
