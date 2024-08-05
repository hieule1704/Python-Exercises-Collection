import math
def tinhDoDai2Diem(xA,yA,xB,yB):
    doDai = math.sqrt((xB-xA)**2 + (yB-yA)**2)
    return doDai

xA = int(input("Nhập tọa độ của x của điểm thứ nhất: "))
yA = int(input("Nhập tọa độ của y của điểm thứ nhất: "))
xB = int(input("Nhập tọa độ của x của điểm thứ hai: "))
yB = int(input("Nhập tọa độ của y của điểm thứ hai: "))

doDai = tinhDoDai2Diem(xA,yA,xB,yB)
print("Độ dài khoảng cách 2 điểm A và B là:",doDai)