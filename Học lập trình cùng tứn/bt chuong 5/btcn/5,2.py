def nhap():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        L=L+[int(input())]
    return L
def Search(L):
    a=min(L)
    b=max(L)
    return a,b
def Output(b,a):
    print(b,a)
L=nhap()
a,b=Search(L)
Output(b,a)
