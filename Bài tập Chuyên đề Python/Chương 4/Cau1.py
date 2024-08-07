#Viết hàm tính diện tích tam giác
import math
def kiemTraTamGiac(a, b, c):
    """Nếu có 1 cạnh có chiều dài lớn hơn tổng chiều dài 2 cạnh còn lại thì ko thỏa"""
    if(a >= b+c or b >= a+c or c >= a+b) or (a<=0 or b<=0 or c<=0):
        return False
    return True

def tinhChuViTamGiac(canh1, canh2, canh3):
    return canh1+canh2+canh3

def tinhDienTichTamGiac(canh1, canh2, canh3):
    nuaChuVi = tinhChuViTamGiac(canh1, canh2, canh3)/2
    dienTich = math.sqrt(nuaChuVi*(nuaChuVi-canh1)*(nuaChuVi-canh2)*(nuaChuVi-canh3))
    return dienTich

#Main
while True:
    print("Nhập thông tin chiều dài các cạnh của tam giác: ")
    canh1 = float(input("Nhập cạnh 1: "))
    canh2 = float(input("Nhập cạnh 2: "))
    canh3 = float(input("Nhập cạnh 3: "))
    if not kiemTraTamGiac(canh1,canh2,canh3):
        print("Tam giác bạn vừa nhập không hợp lệ vui lòng nhập lại")
        continue
    dienTich = tinhDienTichTamGiac(canh1,canh2,canh3)
    print(f"Diện tích tam giác bạn vừa nhập là: {dienTich:<2}")
    flag = input("Nhấn 'q' để dừng chương trình, phím bất kỳ để tiếp tục: ")
    if flag == 'q':
        break



