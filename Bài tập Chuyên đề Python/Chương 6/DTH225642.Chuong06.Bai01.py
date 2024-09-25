# Xử lý list
import math

def check_native_number(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

def input_list():
    list_num = []
    while True:
        try:
            num = int(input("Enter a number, ortherwise enter a character to quit: "))
        except ValueError:
            return list_num
        else:
            list_num.append(num)

def main():
    list_num = input_list()
    char_k = int(input("Enter the number you want to count the occurrences of: "))
    print(f"Number of occurrences of {char_k} is {list_num.count(char_k)}")
    sum = 0
    for i in list_num:
        if check_native_number(i):
            sum += i
    print(f"Sum value of native number is {sum}")
    print("Mảng trước khi sắp xếp:",list_num)
    print("Mảng sau khi sắp xếp tăng dần:", sorted(list_num) ) # Nếu dùng list_num.sort() thì phải ghi thêm 1 dòng riêng với lúc in ra
    del list_num

if __name__ == '__main__':
    main()  

