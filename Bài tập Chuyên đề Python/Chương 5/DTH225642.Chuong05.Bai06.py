def input_string(string_store):
    while True:
        char = input("Enter your number, enter 'quit' to quit: ")
        if char == 'quit':
            return ''.join(string_store) # Hàm join chỉ join kiểu dử liệu chuổi, join int sẽ lỗi
        else:
            string_store.append(char)


def nagative_number_in_string(string):
    nagative_numbers = []
    for i in range(len(string)):
        if string[i] == '-':
            if string[i+1].isdigit():
                num = check_next_number(string[i+1:len(string)-1]) * (-1)
                nagative_numbers.append(num)
    return nagative_numbers

def check_next_number(string):
    num = []
    for i in range(len(string)):
        if string[i].isdigit():
            num.append(string[i])
        else:
            break

    sum = ''.join(num)
    return int(sum)
def main():
    string_store = []
    string_store = input_string(string_store)
    nagative_number = nagative_number_in_string(string_store)
    print(nagative_number)


if __name__ == '__main__':
    main()