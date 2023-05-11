n=int(input())
L=[]
for i in range(1,n+1):
        h=int(input())
        L+=[h]
def count(L):
    dem=0
    for i in L:
        dem=dem+1
    print(dem)
count(L)
# L=[]
# n=int(input('n='))
# for i in range(1,n+1):
#     a=int(input())
#     L=L+[a]
# def count(L):
#     a=0
#     for i in range(len(L)):
#         a=a+1
#     return a

# a=count(L)
# print(a)