# Trong Python, có một số cách để nhập dữ liệu từ bàn phím. Dưới đây là các phương pháp phổ biến nhất:

# 1. Sử dụng hàm input() (nhập dữ liệu dưới dạng chuỗi)
#    - Hàm input() cho phép người dùng nhập dữ liệu từ bàn phím dưới dạng chuỗi.
#    - Ví dụ:
name = input("Nhập tên của bạn: ")
print("Xin chào, " + name)
#    - Khi chạy đoạn mã này, Python sẽ yêu cầu người dùng nhập tên và hiển thị thông báo chào.

# 2. Nhập dữ liệu kiểu số (sử dụng int() hoặc float() để chuyển đổi dữ liệu)
#    - Nếu muốn nhập số nguyên hoặc số thực từ bàn phím, có thể sử dụng int() hoặc float() để chuyển đổi.
#    - Ví dụ (nhập số nguyên):
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn là:", age)
#    - Ví dụ (nhập số thực):
height = float(input("Nhập chiều cao của bạn (m): "))
print("Chiều cao của bạn là:", height, "m")

# 3. Nhập nhiều giá trị cùng lúc (sử dụng split())
#    - Để nhập nhiều giá trị từ một dòng duy nhất, có thể sử dụng hàm split() để tách dữ liệu.
#    - Ví dụ:
data = input("Nhập tên và tuổi của bạn, cách nhau bởi khoảng trắng: ").split()
name = data[0]
age = int(data[1])
print(f"Tên của bạn: {name}, Tuổi của bạn: {age}")
#    - Người dùng nhập dữ liệu theo định dạng: "Tên Tuổi", và dữ liệu sẽ được tách thành hai phần.

# 4. Nhập danh sách giá trị (sử dụng map() và split())
#    - Có thể sử dụng hàm map() để chuyển đổi nhiều giá trị nhập vào thành một danh sách các số.
#    - Ví dụ:
numbers = list(map(int, input("Nhập các số cách nhau bởi khoảng trắng: ").split()))
print("Danh sách các số:", numbers)
#    - Ví dụ này sẽ nhập một chuỗi các số từ bàn phím, sau đó tách và chuyển chúng thành danh sách các số nguyên.

# 5. Nhập dữ liệu Boolean
#    - Nhập dữ liệu Boolean có thể thực hiện bằng cách chuyển đổi chuỗi nhập vào thành True hoặc False.
#    - Ví dụ:
is_student = input("Bạn có phải là học sinh không (True/False)? ").lower() == 'true'
print("Bạn là học sinh:", is_student)
#    - Phần `.lower()` giúp xử lý trường hợp người dùng nhập 'True' hoặc 'true' (không phân biệt hoa thường).
