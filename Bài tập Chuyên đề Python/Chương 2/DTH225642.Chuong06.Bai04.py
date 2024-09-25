# Python hỗ trợ nhiều kiểu dữ liệu cơ bản, mỗi kiểu phục vụ cho các mục đích khác nhau trong lập trình.
# Dưới đây là các kiểu dữ liệu cơ bản trong Python:

# 1. Kiểu số (Numeric Types)
#    - int: Số nguyên, ví dụ: 1, 42, -7.
#    - float: Số thực (số có dấu thập phân), ví dụ: 3.14, -0.001.
#    - complex: Số phức, ví dụ: 1 + 2j, với j là phần ảo.

# 2. Kiểu chuỗi (String Type)
#    - str: Chuỗi ký tự, biểu diễn một dãy các ký tự Unicode. Chuỗi được đặt trong dấu nháy đơn ('...')
#           hoặc dấu nháy kép ("...").
#      Ví dụ: "Hello, world!", 'Python'.

# 3. Kiểu Boolean (Boolean Type)
#    - bool: Chỉ có hai giá trị: True và False. Đây là kiểu dữ liệu nhị phân dùng để lưu trữ kết quả
#            của các phép so sánh hay điều kiện logic.

# 4. Kiểu danh sách (Sequence Types)
#    - list: Danh sách có thể thay đổi (mutable), chứa các phần tử có thể là các kiểu dữ liệu khác nhau.
#      Ví dụ: [1, 2, 3], ['apple', 'banana', 'cherry'].
#    - tuple: Một danh sách nhưng không thể thay đổi (immutable), một khi đã tạo ra không thể chỉnh sửa
#             các phần tử.
#      Ví dụ: (1, 2, 3), ('apple', 'banana', 'cherry').
#    - range: Một dãy số nguyên, thường được sử dụng trong các vòng lặp.
#      Ví dụ: range(5) (tạo ra dãy số từ 0 đến 4).

# 5. Kiểu ánh xạ (Mapping Type)
#    - dict: Từ điển (dictionary) chứa các cặp khóa-giá trị, trong đó mỗi khóa ánh xạ tới một giá trị.
#      Ví dụ: {'name': 'John', 'age': 30}.

# 6. Kiểu tập hợp (Set Types)
#    - set: Tập hợp các phần tử không trùng lặp, không có thứ tự. Các phần tử của set phải là các kiểu
#           dữ liệu bất biến.
#      Ví dụ: {1, 2, 3}, {'apple', 'banana', 'cherry'}.
#    - frozenset: Giống như set nhưng bất biến, tức không thể thay đổi sau khi đã tạo ra.

# 7. Kiểu None (None Type)
#    - NoneType: Chỉ có giá trị duy nhất là None, biểu diễn cho một giá trị rỗng hoặc không tồn tại.
#      Ví dụ: x = None.

# 8. Kiểu nhị phân (Binary Types)
#    - bytes: Chuỗi các byte không thể thay đổi, thường được sử dụng để xử lý dữ liệu nhị phân.
#      Ví dụ: b'hello'.
#    - bytearray: Chuỗi byte có thể thay đổi.
#      Ví dụ: bytearray(b'hello').
#    - memoryview: Cung cấp khả năng truy cập cấp thấp vào dữ liệu nhị phân của các đối tượng hỗ trợ
#                  giao thức bộ nhớ.

# 9. Kiểu Enums (Liệt kê)
#    - enum.Enum: Định nghĩa các hằng số có giá trị cố định trong một nhóm.

# Python còn hỗ trợ nhiều kiểu dữ liệu phức tạp hơn, nhưng các kiểu dữ liệu trên là các kiểu cơ bản nhất
# thường gặp trong lập trình hàng ngày.