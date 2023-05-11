def nhap():
    A=[]
    n=int(input('n='))
    for i in range(1,n+1):
        A=A+[int(input())]
    A.reverse()
    B=A
    return B
def show(B):
    print(B)
    B.sort()
    print(B)
B=nhap()
show(B)