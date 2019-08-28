import os
os.chdir(r'C:\Users\CHANDRU\Python-3-basics-series\file_operations')
with open ('sample.txt') as f:
    count = 0
    for i in f.read():
        if i.isupper():
            count += 1
    print(count)
