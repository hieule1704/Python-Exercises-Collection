#Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. 
#A và B được nhập bất kỳ từ bàn phím. Hiển thị số A sau khi được làm tròn ra màn hình.
print("Nhập số thập phân: ")
number=float(input())
print("Làm trón đến: ")
dot=int(input())
formatted_number = '{0:.{1}f}'.format(number, dot)
print(formatted_number)

"""Cach 2:
print("Nhập số thập phân: ")
soA=float(input()
soB=round(soA,2)
print(soB)
"""

