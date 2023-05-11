def nhap():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        L=L+[int(input())]
    return L
def TinhTongPTchan(L):
    s=0
    for i in range(0,len(L)):
        if i%2!=0:
            s=s+L[i]
    print('Tong=',s,sep='')
L=nhap()
TinhTongPTchan(L)