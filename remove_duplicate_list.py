def remove(l):
    e = []
    for i in l:
        if i not in e:
            e.append(i)
    return e
l =  [12,24,35,24,88,120,155,88,120,155]  
print(remove(l))
    
