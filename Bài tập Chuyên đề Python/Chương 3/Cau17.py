#Viết lại coding dưới đa bằng cách dùng tử khóa break thay thế cho biến done
#Hàm này cho phép n nhận giá trị từ 0 đến 99 ngoài các giá trị này chương trình kết thúc
# done = False
# n, m = 0, 100
# while not done and n!=m:
#     n = int(input("Nhập n: "))
#     if n < 0:
#         done = True
#     print("n =", n)

n, m = 0, 100
while n != m:
    n = int(input("Nhập n: "))
    print(n)
    if n < 0:
        break