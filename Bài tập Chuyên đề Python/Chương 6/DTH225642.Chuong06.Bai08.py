# Hàm nhập vào danh sách các số thực
def input_numbers():
    n = int(input("Nhập số lượng phần tử: "))
    M = []
    for i in range(n):
        number = float(input(f"Nhập số thực M[{i}]: "))
        M.append(number)
    return M

# Hàm sắp xếp danh sách theo thứ tự giảm dần
def sort_descending(M):
    M.sort(reverse=True)  # Sử dụng hàm sort với reverse=True để sắp xếp giảm dần
    return M

# Hàm chính để thực thi chương trình
def main():
    M = input_numbers()
    M = sort_descending(M)
    print("Dãy số sau khi sắp xếp giảm dần:")
    print(M)

if __name__ == "__main__":
    main()
