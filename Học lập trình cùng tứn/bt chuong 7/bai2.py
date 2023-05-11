k='   Xin Chào , tôi là sInh viêN    '
k=k.lower() #viết thường lại hết
k=k.strip() #xóa những dấu cách đầu và cuối str
k=k.split() #xóa những dấu cách thừa
k[0]=k[0].capitalize()
k=' '.join(k)
k=k.replace(' ,', ',').replace(' ;', ';').replace(' :', ':').replace(' .', '.')
print(k)
