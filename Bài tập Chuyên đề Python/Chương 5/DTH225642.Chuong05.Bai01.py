def kiemTraChuoiDoiXung(string):
    length = len(string)
    flag = True
    for i in range(length//2):
        if string[i] != string[length-i-1]:
            flag = False
            return flag
    return flag

#Main
while True:
    str = input("Nhập vào chuổi can kiem tra: ")
    if kiemTraChuoiDoiXung(str):
        print("Chuoi ban vua nhap vao la doi xung!")
    else:
        print("Chuoi ban vua nhap vao khong doi xung!")
    flag = input("Tiep tuc hoac ket thuc(yes/no): ")
    if flag.lower() == "no":
        break