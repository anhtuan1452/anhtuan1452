def stt():
    st=input()
    x=str(input())
    st=st.split(' ')
    dem=0
    k=0
    for i in st:
        if i==x:
            print(dem+1)
            k=1
        dem+=1
    if k!=1:
        print(0)
stt()