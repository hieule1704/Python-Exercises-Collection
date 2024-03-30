#Viết chương trình tính và hiển thị ra màn hình tổng hai số nguyên được nhập bất kỳ từ bàn phím (Có xử lý ngoại lệ đầu vào).
print("Nhập số nguyên thứ nhất: ")
a = input()
print("Nhập số nguyên thứ hai: ")
b = input()
try: #Khối lệnh có thể phát sinh ra lỗi
    so1=int(a)
    so2=int(b)
    tong=so1+so2
except:
    print("Định dạng đầu vào của 2 số nguyên không hợp lệ")
else:
    print("Tổng của 2 số nguyên là:",tong)