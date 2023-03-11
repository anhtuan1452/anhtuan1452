n=int(input('n='))
s=0
for i in range (2,n):
    if n%i==0:
     s=s+1
if s>0 :
    print(n,'khong la SNT')
else:
    print(n,'la SNT')
        