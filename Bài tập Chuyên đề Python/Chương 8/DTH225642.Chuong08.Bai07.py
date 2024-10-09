import tkinter as tk

# Danh sách Thiên can và Địa chi
can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

# Hàm chuyển năm Dương lịch sang Âm lịch
def convert():
    try:
        year = int(entry.get())
        can_index = (year - 3) % 10
        chi_index = (year - 3) % 12
        result = f"{can[can_index]} {chi[chi_index]}"
        label_result.config(text=f"Năm âm: {result}")
    except ValueError:
        label_result.config(text="Vui lòng nhập một số nguyên hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi năm Dương lịch sang Âm lịch")

# Tạo frame để chứa các thành phần giao diện
frame = tk.Frame(root, bg="yellow")
frame.pack(padx=20, pady=20)

# Nhãn và ô nhập cho năm Dương lịch
label_input = tk.Label(frame, text="Nhập năm dương:", bg="yellow", font=("Arial", 12))
label_input.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 12))
entry.grid(row=0, column=1, padx=10, pady=10)

# Nút chuyển đổi
button_convert = tk.Button(frame, text="Chuyển", command=convert, font=("Arial", 12))
button_convert.grid(row=0, column=2, padx=10, pady=10)

# Nhãn kết quả
label_result = tk.Label(frame, text="Năm âm:", bg="yellow", font=("Arial", 12))
label_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Bắt đầu vòng lặp sự kiện chính
root.mainloop()
