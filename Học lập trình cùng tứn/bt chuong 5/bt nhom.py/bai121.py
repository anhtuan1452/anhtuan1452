def nhap():
    L=[]
    n=int(input('độ dài của chuỗi là:'))
    print('các phần tử của chuỗi là:')
    for i in range(1,n+1):
        L=L+[int(input())]
    print(L)
    return L
def doancancat(L):
    print('lay cac ky tu:')
    min=int(input('>= ky tu thu:'))
    max=int(input('< ky tu thu:'))
    return min,max
def chuoiduoclayve(min,max):
    print(L[min-1:max-1])
L=nhap()
min,max=doancancat(L)
chuoiduoclayve(min,max)    
    