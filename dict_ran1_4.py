'''
Define a function which can print a dictionary where the keys are numbers between 1 and
 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
'''

# decalring dictionary function
def dict_fun(x):
    if x in range(1,4):
        d = dict() #defining
        d[x]= x**2
        print(d)

def main():
    for x in range(1,4):
        dict_fun(x)
    
if __name__=="__main__":
    main()
