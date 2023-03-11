n=int(input())
while n>=0:
    if n==0:
         n=1
    i=n-1
    while i>0:
        n=n*i
        i=i-1
    print(n)
    n=int(input())


    