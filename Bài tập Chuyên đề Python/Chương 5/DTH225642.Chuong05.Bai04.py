# Python cung cấp rất nhiều hàm và phương thức để xử lý chuỗi. Dưới đây là một số hàm quan trọng thường được sử dụng:
#
# ### 1. `len()`
# - **Mô tả:** Trả về độ dài của chuỗi, tức là số lượng ký tự trong chuỗi.
# - **Ví dụ:**
#   ```python
#   text = "Hello, Python!"
#   print(len(text))  # Output: 13
#   ```
#
# ### 2. `str()`
# - **Mô tả:** Chuyển đổi các kiểu dữ liệu khác thành chuỗi.
# - **Ví dụ:**
#   ```python
#   number = 123
#   text = str(number)
#   print(text)  # Output: "123"
#   ```
#
# ### 3. `lower()`
# - **Mô tả:** Chuyển đổi tất cả các ký tự trong chuỗi thành chữ thường.
# - **Ví dụ:**
#   ```python
#   text = "Hello, Python!"
#   print(text.lower())  # Output: "hello, python!"
#   ```
#
# ### 4. `upper()`
# - **Mô tả:** Chuyển đổi tất cả các ký tự trong chuỗi thành chữ hoa.
# - **Ví dụ:**
#   ```python
#   text = "Hello, Python!"
#   print(text.upper())  # Output: "HELLO, PYTHON!"
#   ```
#
# ### 5. `replace()`
# - **Mô tả:** Thay thế tất cả các lần xuất hiện của một chuỗi con trong chuỗi bằng một chuỗi khác.
# - **Ví dụ:**
#   ```python
#   text = "Hello, Python!"
#   print(text.replace("Python", "World"))  # Output: "Hello, World!"
#   ```
#
# ### 6. `strip()`
# - **Mô tả:** Loại bỏ khoảng trắng hoặc các ký tự cụ thể ở đầu và cuối chuỗi.
# - **Ví dụ:**
#   ```python
#   text = "  Hello, Python!  "
#   print(text.strip())  # Output: "Hello, Python!"
#   ```
#
# ### 7. `split()`
# - **Mô tả:** Tách chuỗi thành danh sách các phần tử dựa trên ký tự phân cách.
# - **Ví dụ:**
#   ```python
#   text = "apple,banana,cherry"
#   fruits = text.split(',')
#   print(fruits)  # Output: ['apple', 'banana', 'cherry']
#   ```
#
# ### 8. `join()`
# - **Mô tả:** Nối các phần tử của một danh sách thành một chuỗi, với một ký tự phân cách giữa các phần tử.
# - **Ví dụ:**
#   ```python
#   fruits = ['apple', 'banana', 'cherry']
#   text = ', '.join(fruits)
#   print(text)  # Output: "apple, banana, cherry"
#   ```
#
# ### 9. `find()`
# - **Mô tả:** Tìm vị trí đầu tiên của chuỗi con trong chuỗi gốc. Nếu không tìm thấy, trả về `-1`.
# - **Ví dụ:**
#   ```python
#   text = "Hello, Python!"
#   position = text.find("Python")
#   print(position)  # Output: 7
#   ```
#
# ### 10. `startswith()` và `endswith()`
# - **Mô tả:** Kiểm tra chuỗi có bắt đầu (`startswith`) hoặc kết thúc (`endswith`) bằng một chuỗi con cụ thể hay không.
# - **Ví dụ:**
#   ```python
#   text = "Hello, Python!"
#   print(text.startswith("Hello"))  # Output: True
#   print(text.endswith("!"))        # Output: True
#   ```
#
# ### 11. `capitalize()`
# - **Mô tả:** Viết hoa ký tự đầu tiên của chuỗi, các ký tự khác sẽ được chuyển thành chữ thường.
# - **Ví dụ:**
#   ```python
#   text = "hello, python!"
#   print(text.capitalize())  # Output: "Hello, python!"
#   ```
#
# ### 12. `count()`
# - **Mô tả:** Đếm số lần xuất hiện của một chuỗi con trong chuỗi gốc.
# - **Ví dụ:**
#   ```python
#   text = "banana"
#   print(text.count("a"))  # Output: 3
#   ```
#
# Những hàm này giúp bạn thao tác và xử lý chuỗi một cách hiệu quả trong Python, từ việc tìm kiếm, thay thế, cho đến việc định dạng và phân tích chuỗi.