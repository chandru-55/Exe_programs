'''
Question: 1
​
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
​
​
​
Hints:
Use random.choice() to a random element from a list.'''
'''
import random
x = [1,2,3,4,5,6,7,8,9,10]
ev = [i for i in range(10) if i%2 == 0]
print(random.choice(ev))
'''
'''
Ques: 2
The Fibonacci Sequence is computed based on the following formula:
​
​
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
​
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
​
Example:
If the following n is given as input to the program:
​
7
​
Then, the output of the program should be:
​
0,1,1,2,3,5,8,13
​
​
Hints:
We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.
​
In case of input data being supplied to the question, it should be assumed to be a console input.'''

n = int(input("enter the n number of value:")
l = []
fib = [n for i in range(0,n)]
if n == 0:
    print(l.append(fib))
elif n == 1:
    print(li.append(fib))
elif n>1:
    li = (n-1)+(n-2)
    print(li.append(fib))
else:
    print("*****")
        
