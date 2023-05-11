def nhap():
    L=[]
    k=[]
    dem=0
    s=0
    dem1=0
    n=int(input('n='))
    for i in range(1,n+1):
        k=int(input())
        L=L+[k]
        if k>0:
            dem+=1
        if k%2==0:
            s+=k
            dem1+=1
    if dem1==0:
        a=0
    else:
        a=s/dem1
    return dem,a
def show(dem,a):
    print('SND=',dem,sep='')
    print('TBC=',a,sep='')
dem,a=nhap()
show(dem,a)