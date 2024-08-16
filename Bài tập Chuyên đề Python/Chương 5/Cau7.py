# Tối ưu chuỗi danh từ
def format_string(string):
    string = string.title().strip().split() # Thứ tự thực hiện các câu lệnh từ phải qua trái title -> strip -> split
    return " ".join(string)
def main():
    string_store = input("Enter a alpha string without special characters: ")
    print(format_string(string_store))

if __name__ == '__main__':
    main()

