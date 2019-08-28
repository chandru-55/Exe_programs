
'''
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1'''
def freq(str):
    str = str.split()
    str1 = []
    for i in str:
        if i not in str1:
            str1.append(i)
    for i in range(0,len(str1)):
        print( str1[i],":", str.count(str1[i]))
def main():
    str = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
    freq(str)
if __name__=="__main__":
    main()
        
