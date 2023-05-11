def kiemtramatkhau():
    import re
    mk=input()
    char=0
    num=0
    cap=0
    kt=0
    if 5<len(mk)<18:
        for i in mk:
            if re.search("[a-z]",i)!=None:
                char=1
            elif re.search("[0-9]",i)!=None:
                num=1
            elif re.search("[A-Z]",i)!=None:
                cap=1
            elif re.search("[@,#,!]",i)!=None:
                kt=1
    else:
        print('False')
    if char==num==cap==kt==1:
        return True
    else:
        return False
k=kiemtramatkhau()
print(k)