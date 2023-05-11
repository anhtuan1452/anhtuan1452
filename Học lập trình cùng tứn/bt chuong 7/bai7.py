in4=input()
k=in4[in4.index('Email:')::]
if len(k)>6:
    in4=in4.split(': ')
    print(k[7::])
else:
    print(' ')