def sum1(n):
    #Hàm này không khai báo  global nên mọi thay đổi voi biến n hay biến global trong main
    #đều không ảnh hưởng đến giá trị
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s
def sum2():
    """Hàm nay có gọi global nên cho python biet val la bien toàn cục
    mọi thay đổi trong hàm đều ảnh hưởng đến biến ở ngoài
    """
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s = 0
    #Tương tự hàm sum1
    for i in range(val, 0, -1):
        s += 1
    return s
#TH1
# def main():
#     global val
#     val = 5
#     print(sum1(5))
#     print(sum2())
#     print(sum3())
# def main():
#     global val
#     val = 5
#     print(sum1(5))
#     print(sum3())
#     print(sum2())

def main():
    global val
    val = 5
    print(sum2())
    print(sum1(val))
    print(sum3())

main()