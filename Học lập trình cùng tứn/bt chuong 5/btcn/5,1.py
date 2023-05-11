def nhap():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        L=L+[int(input())]
    return L
def FirstAndLast(L):
    S=[]
    x=int(input('x='))
    S.append(L[0])
    S.append(L[-1])
    print(S)
    return x
def Search(L,x):
    print(x in L)
L=nhap()    
x=FirstAndLast(L)
Search(L,x)