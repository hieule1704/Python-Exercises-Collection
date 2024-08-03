a = int(input("Nhập giá trị của a : "))
b = int(input("Nhập giá trị của b : "))
while True:
    math = str(input("Vui lòng nhập 1 trong 4 phép tính sau: + - * /"))
    if(math=='+'):
        print(a+b)
        break
    elif(math=='-'):
        print(a-b)
        break
    elif(math=='*'):
        print(a*b)
        break
    elif(math=='/'):
        print(a/b)
        break
    else:
        print("Phép tính bạn vừa nhập không hợp lệ vui lòng nhập lại!")
