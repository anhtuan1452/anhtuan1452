x=int(input())
n=int(input())
L=[]
for i in range(1,n+1):
        h=int(input())
        L+=[h]
def delete(L,x):
    K=[]
    for i in L:
        if i!=x:
            K=K+[i]
    print(K)
delete(L,x)
