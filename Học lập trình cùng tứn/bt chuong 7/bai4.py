def xulychuoi():
    l =input()
    l = l.split(',')
    i = 0
    a=[]
    while i < len(l):
        if l[i] not in a:
            a.append(l[i])
        i+=1
    a.sort()
    a=','.join(a)
    return a
    
        

a = xulychuoi()
print(a)

        