import math
def kiemTraSoNguyenTo(x):
    if(x<=1):
        return False
    canTren = int(math.sqrt(x))
    for i in range(2,canTren):
        if(x%i==0):
            return False
    return True

#Main
while True:
    x = int(input("Nhập số cần kiểm tra số nguyên tố: "))
    if kiemTraSoNguyenTo(x):
        print(f"{x} là số nguyên tố")
    else:
        print("{0} không phải là số nguyên tố".format(x))
    flag = input("Nhấn q để kết thúc chương trình! Gõ phím bất kỳ để tiếp tục")
    if(flag.lower() == 'q'):
        break
