n=int(input('n='))
s=1
for i in range(n,0,-1):
    s=i*s
print(n,'!=',s,sep='')
    