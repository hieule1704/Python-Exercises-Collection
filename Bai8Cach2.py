#Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, 
#dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng. Tính tổng của dãy số và hiển thị ra màn hình.
print("Nhập dãy số nguyên cách nhau bởi khoảng trắng: ")
daySo=input()
danhSachGiaTri=daySo.split()
tongDaySo= map(int,danhSachGiaTri)
print("Tổng của dãy số là: ",sum(tongDaySo))