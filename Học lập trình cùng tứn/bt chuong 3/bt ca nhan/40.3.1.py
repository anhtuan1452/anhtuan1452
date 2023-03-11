import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
p=(a+b+c)/2
b=math.sqrt(p*(p-a)*(p-b)*(p-c))
if ((a+b)>c and (a+c)>b and (b+c)>a) :
    print('Dientich=',round(b,3))
else:
    print('Khong hop le')