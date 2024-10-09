import tkinter as tk


# Hàm tính BMI và hiển thị kết quả
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / (height ** 2)
        label_bmi_value.config(text=f"{bmi:.2f}")

        # Xác định tình trạng sức khỏe dựa trên giá trị BMI
        if bmi < 18.5:
            status = "Gầy"
            risk = "Thấp"
        elif 18.5 <= bmi < 24.9:
            status = "Bình thường"
            risk = "Trung bình"
        elif 25 <= bmi < 29.9:
            status = "Hơi béo"
            risk = "Hơi cao"
        else:
            status = "Béo phì"
            risk = "Cao"

        label_status_value.config(text=status)
        label_risk_value.config(text=risk)
    except ValueError:
        label_bmi_value.config(text="Lỗi!")
        label_status_value.config(text="Lỗi!")
        label_risk_value.config(text="Lỗi!")


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Phần mềm tính BMI")

# Tạo frame để chứa các thành phần giao diện
frame = tk.Frame(root, bg="yellow")
frame.pack(padx=20, pady=20)

# Nhập chiều cao
label_height = tk.Label(frame, text="Nhập chiều cao (m):", bg="yellow", font=("Arial", 12))
label_height.grid(row=0, column=0, padx=10, pady=10)

entry_height = tk.Entry(frame, font=("Arial", 12))
entry_height.grid(row=0, column=1, padx=10, pady=10)

# Nhập cân nặng
label_weight = tk.Label(frame, text="Nhập cân nặng (kg):", bg="yellow", font=("Arial", 12))
label_weight.grid(row=1, column=0, padx=10, pady=10)

entry_weight = tk.Entry(frame, font=("Arial", 12))
entry_weight.grid(row=1, column=1, padx=10, pady=10)

# Nút tính BMI
button_calculate = tk.Button(frame, text="Tính BMI", command=calculate_bmi, font=("Arial", 12))
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Kết quả BMI
label_bmi = tk.Label(frame, text="BMI của bạn:", bg="yellow", font=("Arial", 12))
label_bmi.grid(row=3, column=0, padx=10, pady=10)

label_bmi_value = tk.Label(frame, text="x", bg="yellow", font=("Arial", 12))
label_bmi_value.grid(row=3, column=1, padx=10, pady=10)

# Tình trạng sức khỏe
label_status = tk.Label(frame, text="Tình trạng của bạn:", bg="yellow", font=("Arial", 12))
label_status.grid(row=4, column=0, padx=10, pady=10)

label_status_value = tk.Label(frame, text="x", bg="yellow", font=("Arial", 12), fg="red")
label_status_value.grid(row=4, column=1, padx=10, pady=10)

# Nguy cơ phát triển bệnh
label_risk = tk.Label(frame, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("Arial", 12))
label_risk.grid(row=5, column=0, padx=10, pady=10)

label_risk_value = tk.Label(frame, text="x", bg="yellow", font=("Arial", 12), fg="red")
label_risk_value.grid(row=5, column=1, padx=10, pady=10)

# Nút thoát
button_exit = tk.Button(frame, text="Thoát", command=root.quit, font=("Arial", 12))
button_exit.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Bắt đầu vòng lặp sự kiện chính
root.mainloop()
