a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
max=a
min=c
if (b>max) :
    max=b
if (c> max):
    max=c
print('SLN=',max,sep='')
if (a<min) :
    min=a
if (b< min):
    min=b
print('SBN=',min,sep='')

