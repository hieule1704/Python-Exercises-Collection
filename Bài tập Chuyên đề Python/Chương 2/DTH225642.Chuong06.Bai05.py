# Trong Python, có ba loại ghi chú (comment) chính mà bạn có thể sử dụng để giải thích mã
# hoặc tạm thời vô hiệu hóa một số phần mã.

# 1. Ghi chú một dòng (Single-line comment)
#    - Ghi chú một dòng được bắt đầu bằng dấu thăng (#).
#    - Toàn bộ nội dung sau dấu # trên cùng một dòng sẽ được Python bỏ qua khi chạy mã.
#    - Ví dụ:
#      # Đây là ghi chú một dòng.
#      x = 5  # Ghi chú cũng có thể đứng sau một dòng lệnh.

# 2. Ghi chú nhiều dòng bằng nhiều dấu thăng (Multi-line comment using #)
#    - Không có cú pháp riêng cho ghi chú nhiều dòng, nhưng bạn có thể sử dụng nhiều dấu thăng (#)
#      để viết ghi chú trên nhiều dòng liên tiếp.
#    - Ví dụ:
#      # Đây là dòng ghi chú đầu tiên.
#      # Đây là dòng ghi chú thứ hai.
#      # Đây là dòng ghi chú thứ ba.

# 3. Ghi chú nhiều dòng bằng chuỗi ký tự (Multi-line comment using string literals)
#    - Bạn có thể sử dụng các chuỗi ký tự dài ('''...''' hoặc """...""") để tạo ghi chú nhiều dòng.
#    - Thông thường, các chuỗi này được dùng cho docstring (tài liệu hàm), nhưng khi không được gán
#      cho biến hay dùng làm docstring, chúng sẽ được Python bỏ qua.
#    - Ví dụ:
#      '''
#      Đây là một ghi chú nhiều dòng.
#      Nó có thể chiếm nhiều dòng trong mã của bạn.
#      '''
#    - Ghi chú kiểu này có thể được sử dụng để ghi chú dài dòng hoặc mô tả các phần lớn trong mã.

# Python không có ghi chú kiểu /* ... */ như trong các ngôn ngữ lập trình C hoặc Java.
