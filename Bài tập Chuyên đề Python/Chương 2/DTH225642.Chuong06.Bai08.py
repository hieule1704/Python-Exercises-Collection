
# Trong lập trình, có nhiều loại lỗi có thể xảy ra. Dưới đây là các loại lỗi phổ biến trong Python và
# cách xử lý chúng bằng việc bắt lỗi (exception handling).

# 1. Lỗi cú pháp (SyntaxError)
#    - Lỗi xảy ra khi mã nguồn vi phạm quy tắc cú pháp của Python.
#    - Ví dụ:
#      print("Hello, world"  # Thiếu dấu ngoặc đóng sẽ gây ra lỗi SyntaxError
#    - Python không thể chạy mã có lỗi cú pháp, nên cần sửa lại mã trước khi chạy.

# 2. Lỗi thời gian chạy (RuntimeError)
#    - Lỗi xảy ra khi chương trình đang chạy và gặp phải các tình huống bất ngờ, như phép chia cho 0
#      hoặc truy cập vào biến chưa được khởi tạo.
#    - Ví dụ:
x = 10 / 0  # Lỗi ZeroDivisionError do chia cho 0

# 3. Lỗi ngoại lệ (Exception)
#    - Ngoại lệ là một loại lỗi xảy ra trong quá trình chạy chương trình, nhưng có thể được xử lý để
#      chương trình không bị dừng đột ngột.
#    - Ví dụ:
try:
    number = int(input("Nhập một số nguyên: "))
    result = 10 / number
    print(f"Kết quả của 10 chia cho {number} là: {result}")
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except Exception as e:
    print(f"Một lỗi không xác định đã xảy ra: {e}")

# 4. Lỗi logic (Logic Error)
#    - Lỗi logic là lỗi xảy ra khi chương trình không cho kết quả đúng như mong đợi,
#      mặc dù không có lỗi cú pháp hay ngoại lệ nào được sinh ra.
#    - Ví dụ:
#      Giả sử muốn tính tổng của các số từ 1 đến 10 nhưng chương trình lại tính sai:
total = 0
for i in range(1, 11):
    total += i * i  # Lỗi logic: tính tổng bình phương thay vì tổng số
print(f"Tổng là: {total}")
#    - Trong trường hợp này, chương trình vẫn chạy nhưng cho ra kết quả không chính xác.

# 5. Cách bắt lỗi trong Python (Exception Handling)
#    - Python cung cấp cơ chế bắt và xử lý ngoại lệ bằng các khối `try`, `except`, `else`, và `finally`.
#    - Ví dụ về cách bắt lỗi:
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    result = a / b
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0.")
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
else:
    print(f"Kết quả: {a} / {b} = {result}")
finally:
    print("Chương trình đã kết thúc.")

#    - Cấu trúc của khối try-except:
#      + `try`: Chứa các đoạn mã có khả năng gây ra ngoại lệ.
#      + `except`: Xử lý các ngoại lệ xảy ra trong khối `try`.
#      + `else`: Chạy nếu không có ngoại lệ nào xảy ra trong khối `try`.
#      + `finally`: Chạy trong mọi trường hợp, dù có hay không có ngoại lệ.

# Tóm lại, việc bắt lỗi (exception handling) giúp chương trình có thể xử lý các tình huống không mong muốn
# mà không bị gián đoạn. Nó là một phần quan trọng trong việc viết mã Python ổn định và bảo mật.
