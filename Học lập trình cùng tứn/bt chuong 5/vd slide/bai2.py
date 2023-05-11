x=int(input())
n=int(input())
L=[]
for i in range(1,n+1):
        h=int(input())
        L+=[h]
def search(L,x):
    dem=0
    for i in range(0,len(L)):
        if L[i]==x:
            print(i,end=' ')
            dem=dem+1
    if dem==0:
        print(None,end=' ')
search(L,x)