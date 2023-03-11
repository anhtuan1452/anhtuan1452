m1=int(input('M1='))
m2=int(input('M2='))
m3=int(input('M3='))
s=int(input('S='))
if (s<=100) :
    print('Phai tra=',s*m1,sep='')
elif(100<s<=150) :
    print('Phai tra=',(100*m1)+(s-100)*m2,sep='')
elif (s>150):
    print('Phai tra=',(100*m1)+(50*m2)+(s-150)*m3,sep='')
