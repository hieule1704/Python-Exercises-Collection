import math

def nested_sqrt(x, n):
    if n == 1:
        return math.sqrt(x)
    else:
        return math.sqrt(x+nested_sqrt(x, n-1))

# Ví dụ sử dụng hàm:
x = int(input("Nhập cơ số: "))
n = int(input("Nhập số lần lòng nhau: "))
result = nested_sqrt(x, n)
print(f"Căn bậc 2 lồng nhau {n} lần của {x} là: {result}")
