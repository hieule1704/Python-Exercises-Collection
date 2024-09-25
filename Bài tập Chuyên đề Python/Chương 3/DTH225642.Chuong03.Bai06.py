def doc_so_2_chu_so(n):
    # Danh sách số đọc
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi",
                 "chín mươi"]

    # Xử lý các trường hợp đặc biệt
    if n == 0:
        return "không"
    elif n < 10:
        return don_vi[n]
    else:
        chuc = n // 10
        dv = n % 10
        if dv == 0:
            return hang_chuc[chuc]
        elif dv == 1 and chuc == 1:
            return "mười một"
        elif chuc == 1:
            return "mười " + don_vi[dv]
        elif dv == 1:
            return hang_chuc[chuc] + " mốt"
        elif dv == 5 and chuc != 0:
            return hang_chuc[chuc] + " lăm"
        else:
            return hang_chuc[chuc] + " " + don_vi[dv]


# Nhập số và kiểm tra điều kiện
n = int(input("Nhập một số có tối đa 2 chữ số: "))
if 0 <= n <= 99:
    print(doc_so_2_chu_so(n))
else:
    print("Số nhập vào không hợp lệ. Vui lòng nhập một số từ 0 đến 99.")
