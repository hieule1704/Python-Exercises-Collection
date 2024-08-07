def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def tinhS(x, n):
    """Tính dãy số S(x,n)"""
    s = 0
    for i in range(1,n+1):
        s += x**(i)/factorial_recursive(i)
    return s

#Main
x = int(input("Nhập giá trị của x: "))
n = int(input("Nhập giá tr của n: "))
print(f"Kết quả của phép tính S(x,n) = {tinhS(x, n)}")