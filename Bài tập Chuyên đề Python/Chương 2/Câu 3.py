diemHoa = float(input("Nhập điểm môn Hóa: "))
diemLy = float(input("Nhập điểm môn Lý: "))
diemToan = float(input("Nhập điểm môn Toán: "))
avg = (diemHoa+diemLy+diemToan)/3
#Có nhiêu cách để in ra số thực có 2 số thập phân phía sau
print("Điểm trung bình 3 môn Toán Lý Hóa là {:.2f}".format(avg))
print("Điểm trung bình 3 môn Toán Lý Hóa là: %.2f"%avg)
print("Điểm trung bình 3 môn Toán Lý Hóa là:", f"{avg:.2f}")
print("Điểm trung bình 3 môn Toán Lý Hóa là: ",round(avg,2))
