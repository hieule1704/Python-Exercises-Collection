import math

def log_base(a, b):
    #Hàm log() này tính log với cơ số e tự nhien
    return math.log(a) / math.log(b)

# Ví dụ sử dụng hàm:
a = int(input("Nhập cơ số a: "))
b = int(input("Nhập cơ so b: "))
result = log_base(a, b)
print(f"log cơ số {b} của {a} là: {result}")
