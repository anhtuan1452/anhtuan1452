n=int(input('n='))
L=[]
for i in range(1,n+1):
    L=L+[int(input())]
M=[]
for x in L:
    if x not in M:
        M.append(x)
for i in M:
    print(i,end=' ')
    
















































# j=0
# while j<len(L):
#     a=j+1
#     while a<len(L):
#         if L[j]==L[a]:
#             del(L[a])
#         else:
#             a+=1
#     j+=1
# print(L)