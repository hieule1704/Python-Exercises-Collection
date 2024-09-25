year = int(input("Nhập năm mà bạn muốn kiếm tra: "))
if(year%4 == 0 and year%100 != 0) or year%400 != 0:
    print(year,"là năm nhuận")
else:
    print(year,"không phải là năm nhuận")