np=input()
np=np.split(',')
kq=[]
for i in np:
    int(i)
    k=int(i,2)
    if k%3==0:
        kq=kq+[i]


kq=','.join(kq)
print(kq)