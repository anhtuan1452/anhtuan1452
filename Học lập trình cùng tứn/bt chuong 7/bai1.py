s=input()
Inhoa=0
Inthuong=0
Chuso=0
Khac=0
for i in s:
    if i.isupper()==True:
        Inhoa+=1
    elif i.isnumeric()==True:
        Chuso+=1
    elif i.islower()==True:
        Inthuong+=1
    else:
        Khac+=1
print('In hoa:',Inhoa)
print('In thuong:',Inthuong)
print('Chu so:',Chuso)
print('Khac:',Khac)
    