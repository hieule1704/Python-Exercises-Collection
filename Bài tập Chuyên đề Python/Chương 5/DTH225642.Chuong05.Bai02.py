def formatString(string):
    # Xóa khoảng trắng ở đầu và cuối chuỗi
    string = string.strip()

    # Chuyển chuỗi thành danh sách các ký tự
    strings = list(string)
    index = 0

    # Xóa các khoảng trắng thừa giữa các từ
    while index < len(strings) - 1:
        if strings[index] == ' ' and strings[index + 1] == ' ':
            strings.pop(index)
        else:
            index += 1

    # Chuyển danh sách ký tự trở lại thành chuỗi
    return ''.join(strings)


def main():
    string = input("Enter your string here: ")
    print(id(string)) #In dia chi vung nho của bien
    print("Formatted string:", formatString(string))


if __name__ == '__main__':
    main()
