def chuyendoitrungtosanghauto(bieuthuctrungto):
    toantu = []
    bieuthuchauto = []
    thutuuutien = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for token in bieuthuctrungto:
        if token.isnumeric():
            bieuthuchauto.append(token)
        elif token in thutuuutien:
            while toantu and toantu[-1] != '(' and thutuuutien[token] <= thutuuutien.get(toantu[-1], 0):
                bieuthuc_hau_to.append(toantu.pop())
            toantu.append(token)
        elif token == '(':
            toantu.append(token)
        elif token == ')':
            while toantu and toantu[-1] != '(':
                bieuthuchauto.append(toantu.pop())
            toantu.pop()
    while toantu:
        bieuthuchauto.append(toan_tu.pop())
    return bieuthuchauto

bieuthuctrungto = input("Nhập biểu thức trung tố: ").split()
bieuthuchauto = chuyendoitrungtosanghauto(bieuthuctrungto)
print("Biểu thức hậu tố: ", " ".join(bieuthuchauto))