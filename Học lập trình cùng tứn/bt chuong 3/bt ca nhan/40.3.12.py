n=int(input())
if n<10:
    s=1
elif 10<=n<100:
    s=10
elif 100<=n<1000:
    s=100
elif 1000<n<10000:
    s=1000
while s>=1:
    if n//s==0:
        print('A',end='')
        n=n-s*(n//s)
    elif n//s==1:
        print('B',end='')
        n=n-s*(n//s)
    elif n//s==2:
        print('C',end='')
        n=n-s*(n//s)
    elif n//s==3:
        print('D',end='')
        n=n-s*(n//s)
    elif n//s==4:
        print('E',end='')
        n=n-s*(n//s)
    elif n//s==5:
        print('F',end='')
        n=n-s*(n//s)
    elif n//s==6:
        print('G',end='')
        n=n-s*(n//s)
    elif n//s==7:
        print('H',end='')
        n=n-s*(n//s)
    elif n//s==8:
        print('K',end='')
        n=n-s*(n//s)
    elif n//s==9:
        print('L',end='')
        n=n-s*(n//s)
    s=s/10
