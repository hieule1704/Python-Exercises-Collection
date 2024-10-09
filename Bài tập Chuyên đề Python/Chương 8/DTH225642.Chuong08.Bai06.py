import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Style của Button trong Python")

# Tạo frame để chứa các button
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Danh sách các borderwidth và style
borderwidths = [0, 1, 2, 3, 4]
styles = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

# Tạo các nút button tương ứng với từng borderwidth và style
for i, borderwidth in enumerate(borderwidths):
    for j, style in enumerate(styles):
        btn = tk.Button(frame, text=f"{style}", relief=style, borderwidth=borderwidth, width=8)
        btn.grid(row=i, column=j, padx=5, pady=5)

# Bắt đầu vòng lặp sự kiện chính
root.mainloop()
