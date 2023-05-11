bieuthuc=str(input())
L=list(bieuthuc)
i=1
while i<len(L)-1:
    if L[i-1]=='(' :
        k=L[i+1]
        h=L[i]
        del(L[i+1])
        L[i]=h+k
        
    i+=1
print(L)




            
            