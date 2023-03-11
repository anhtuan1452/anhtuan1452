n='1'
while n!='t' and n!='T':
    a=float(input('a='))
    b=float(input('b='))
    T=str(input('Toan tu:'))
    if T == '+':
        print(a,'+',b,'=',a+b,sep='')
    elif T == '-':
        print(a,'-',b,'=',a-b,sep='')
    elif T == '*':
        print(a,'*',b,'=',a*b,sep='',round=0)
    elif T == '/':
        print(a,'/',b,'=',a/b,sep='')
    n=str(input('Tiep tuc:'))
                
    
    