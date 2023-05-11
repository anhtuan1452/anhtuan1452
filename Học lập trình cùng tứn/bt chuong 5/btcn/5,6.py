def nhap():
    L=[]
    for i in range(1,11):
        L=L+[int(input())]
    return L
def DoiViTri(L):
    i=0
    B=L[:]
    while i<len(L)-1:
        B[i]=L[i+1]
        B[i+1]=L[i]
        i+=2     
    for i in B:
        print(i,end=' ')
B=nhap()
DoiViTri(B)        
    