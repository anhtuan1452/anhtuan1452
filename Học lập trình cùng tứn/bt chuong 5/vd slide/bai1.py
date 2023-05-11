x=int(input())
k=int(input())
n=int(input())
L=[]
for i in range(1,n+1):
        h=int(input())
        L+=[h]
def add(L,x,k):
    L=[]
    L = L[:k] + [x] + L[k:]
    print(L)
add(L,x,k)