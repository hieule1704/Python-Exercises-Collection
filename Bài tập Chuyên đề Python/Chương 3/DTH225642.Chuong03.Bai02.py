#Đếm số ngày trong tháng
while True:
    month = int(input("Nhập tháng: "))
    if month <= 12 and month > 0:
        break
    else:
        print("Tháng bạn vừa nhập không hợp lệ vui lòng nhập lại!")
if month in [4, 6, 9, 11]:
    print(month, "có 30 ngày!")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print(month, "có 31 ngày!")
else:
    year = int(input("Vui lòng nhập thêm năm: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(month, "có 29 ngày!")
    else:
        print(month, "có 28 ngày!")