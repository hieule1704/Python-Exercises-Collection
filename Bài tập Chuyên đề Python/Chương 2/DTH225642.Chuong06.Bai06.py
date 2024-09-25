
# Trong Python, các toán tử /, //, %, **, and, or, is có các ý nghĩa khác nhau, thường được sử dụng
# để thực hiện các phép toán hoặc kiểm tra điều kiện logic.

# 1. Toán tử / (Phép chia thông thường)
#    - Thực hiện phép chia và trả về kết quả dưới dạng số thực (float).
#    - Ví dụ:
#      10 / 3  # Kết quả: 3.3333333333333335

# 2. Toán tử // (Phép chia lấy phần nguyên)
#    - Thực hiện phép chia và chỉ lấy phần nguyên của kết quả.
#    - Ví dụ:
#      10 // 3  # Kết quả: 3

# 3. Toán tử % (Phép chia lấy phần dư)
#    - Trả về phần dư của phép chia.
#    - Ví dụ:
#      10 % 3  # Kết quả: 1

# 4. Toán tử ** (Phép lũy thừa)
#    - Tính lũy thừa của một số, nghĩa là lấy cơ số nâng lên mũ.
#    - Ví dụ:
#      2 ** 3  # Kết quả: 8 (vì 2^3 = 8)

# 5. Toán tử and (Phép toán logic AND)
#    - Trả về True nếu cả hai điều kiện đều đúng (True), ngược lại trả về False.
#    - Ví dụ:
#      True and False  # Kết quả: False
#      True and True   # Kết quả: True

# 6. Toán tử or (Phép toán logic OR)
#    - Trả về True nếu ít nhất một trong hai điều kiện đúng (True), ngược lại trả về False.
#    - Ví dụ:
#      True or False   # Kết quả: True
#      False or False  # Kết quả: False

# 7. Toán tử is (Kiểm tra đồng nhất đối tượng)
#    - Kiểm tra xem hai đối tượng có trỏ đến cùng một vùng nhớ (cùng là một đối tượng) hay không.
#    - Khác với toán tử == (so sánh giá trị), is kiểm tra xem hai biến có phải là cùng một đối tượng không.
#    - Ví dụ:
#      a = [1, 2, 3]
#      b = a
#      a is b  # Kết quả: True (cả a và b cùng trỏ đến một danh sách)
#      a == b  # Kết quả: True (giá trị của a và b giống nhau)
#
#      c = [1, 2, 3]
#      a is c  # Kết quả: False (a và c là hai đối tượng khác nhau)
#      a == c  # Kết quả: True (giá trị của a và c giống nhau)
