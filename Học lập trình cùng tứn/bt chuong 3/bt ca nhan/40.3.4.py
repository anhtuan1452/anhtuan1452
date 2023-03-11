t=int(input())
l=int(input())
h=int(input())
tb=(t*2+l*3+h)/6
if (tb<3):
    print('Kem')
elif (3<=tb<5):
    print('Yeu')
elif (5<=tb<6):
    print('Trung binh')
elif (6<=tb<7):
    print('Trung binh kha')
elif (7<=tb<8):
    print('kha')
elif(8<=tb<9):
    print('gioi')
else :
    print('Xuat sac')