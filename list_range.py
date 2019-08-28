'''Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list'''
def lis_fun(x):
    l = list()
    l.append(x**2)
   # d = x**2
    print(l [0:6])
def main():  
    for x in range(1,21):
        
        lis_fun(x)
if __name__ == "__main__":
    
    main()
