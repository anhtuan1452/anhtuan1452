x=int(input())
k=int(input())
n=int(input())
L=[]
for i in range(1,n+1):
        h=int(input())
        L+=[h]
def update(L,x,k):
    dem=0
    for i in range(0,len(L)):
        if L[i]==x:
            L[i]=k
    print(L)
update(L,x,k)