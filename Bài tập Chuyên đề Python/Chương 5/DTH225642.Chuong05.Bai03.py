# Xu ly tach chuoi
import math
def input_string(string_store):
    while True:
        char = input("Enter your number, enter 'q' to quit: ")
        if char == 'q':
            return ';'.join(string_store) # Hàm join chỉ join kiểu dử liệu chuổi, join int sẽ lỗi
        else:
            string_store.append(char)

def check_character(string):
    list_string = string.split(';')
    count_even_num = 0
    count_odd_num = 0
    count_negative_num = 0
    count_positive_num = 0
    average = 0
    sum = 0
    count_native_num = 0
    for i in list_string:
        i = int(i)
        if i%2 == 0:
            count_even_num += 1
        else:
            count_odd_num += 1
        if i<0:
            count_negative_num += 1
        elif i>0:
            count_positive_num += 1
        if check_native_num(i):
            count_native_num += 1
        sum+=i
    average = sum/len(list_string)
    print(f"Number of even numbers: {count_even_num}"
          f"\nNumber of odd numbers: {count_odd_num}"
          f"\nNumber of negative numbers: {count_negative_num}"
          f"\nNumber of positive numbers: {count_positive_num}"
          f"\nAverage: {average:.2f}"
          f"\nNumber of native numbers: {count_native_num}")
def check_native_num(num):
    if num<2:
        return False
    for i in range(2,int(math.sqrt(num)+1)):
        if(num%i==0):
            return False
    return True
def main():
    string_store = []
    string_store = input_string(string_store)
    check_character(string_store)

if __name__ == '__main__':
    main()