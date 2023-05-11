def nhap():
    L=[]
    n=int(input('độ dài của chuỗi là:'))
    print('các phần tử của chuỗi là:')
    for i in range(1,n+1):
        L=L+[int(input())]
    print(L)
    return L
def kiemtra(L):
    k=L.copy()
    m=L.copy()
    k.sort()
    m.sort(reverse=True) 
    if L==m or L==k:
        print('chuoi da duoc sap xep')
    else:
        print('chuoi chua duoc sap xep')
L=nhap()
kiemtra(L)  