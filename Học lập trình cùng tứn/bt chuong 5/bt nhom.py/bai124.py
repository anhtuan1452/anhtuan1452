
def la_toan_tu(ky_tu):
    toan_tu = ['+', '-', '*', '/']
    return ky_tu in toan_tu
def danh_gia_bieu_thuc_hau_to(bieu_thuc):
    gia_tri = []
    for ky_tu in bieu_thuc:
        if ky_tu.isdigit():
            gia_tri.append(int(ky_tu))
        elif la_toan_tu(ky_tu):
            phai = gia_tri.pop()
            trai = gia_tri.pop()
            if ky_tu == '+':
                gia_tri.append(trai + phai)
            elif ky_tu == '-':
                gia_tri.append(trai - phai)
            elif ky_tu == '*':
                gia_tri.append(trai * phai)
            elif ky_tu == '/':
                gia_tri.append(trai / phai)
    return gia_tri[0]
def trung_to_sang_hau_to(bieu_thuc):
    uu_tien = {'+':1, '-':1, '*':2, '/':2}
    toan_tu = []
    hau_to = []
    for ky_tu in bieu_thuc:
        if ky_tu.isalnum():
            hau_to.append(ky_tu)
        elif ky_tu == '(':
            toan_tu.append(ky_tu)
        elif ky_tu == ')':
            while toan_tu and toan_tu[-1] != '(':
                hau_to.append(toan_tu.pop())
            toan_tu.pop()
        elif la_toan_tu(ky_tu):
            while toan_tu and uu_tien[ky_tu] <= uu_tien.get(toan_tu[-1], 0):
                hau_to.append(toan_tu.pop())
            toan_tu.append(ky_tu)
    while toan_tu:
        hau_to.append(toan_tu.pop())
    return ''.join(hau_to)
def main():
    bieu_thuc_trung_to = input("Nhập biểu thức toán học dưới dạng trung tố: ")
    bieu_thuc_hau_to = trung_to_sang_hau_to(bieu_thuc_trung_to)
    print("Biểu thức hậu tố: ", bieu_thuc_hau_to)
    ket_qua = danh_gia_bieu_thuc_hau_to(bieu_thuc_hau_to)
    print("Kết quả: ", ket_qua)

if __name__ == "__main__":
    main()




