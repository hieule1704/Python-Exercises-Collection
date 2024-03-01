#Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng (Có xử lý ngoại lệ đầu vào).
print("Nhập dãy số nguyên cách nhau bởi khoảng trắng: ")
daySo=input()
try:
    danhSachGiaTri=daySo.split()
    tongDaySo= map(int,danhSachGiaTri)
    print("Tổng của dãy số là: ",sum(tongDaySo))
except:
    print("Gía trị mãng bạn vừa nhập không hợp lệ!")
