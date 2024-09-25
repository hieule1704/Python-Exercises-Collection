import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Hàm nhập vào danh sách các số tự nhiên
def input_numbers():
    n = int(input("Nhập số lượng phần tử: "))
    array = []
    for i in range(n):
        number = int(input(f"Nhập số tự nhiên M[{i}]: "))
        array.append(number)
    return array


# Hàm xử lý và xuất kết quả
def process_and_display(array):
    odd_numbers = [num for num in array if num % 2 != 0]
    even_numbers = [num for num in array if num % 2 == 0]
    prime_numbers = [num for num in array if is_prime(num)]
    non_prime_numbers = [num for num in array if not is_prime(num)]

    # In ra các số lẻ và số lượng
    print("Dòng 1 (Số lẻ):", odd_numbers, f"Tổng cộng có {len(odd_numbers)} số lẻ.")

    # In ra các số chẵn và số lượng
    print("Dòng 2 (Số chẵn):", even_numbers, f"Tổng cộng có {len(even_numbers)} số chẵn.")

    # In ra các số nguyên tố
    print("Dòng 3 (Số nguyên tố):", prime_numbers)

    # In ra các số không phải là số nguyên tố
    print("Dòng 4 (Không phải số nguyên tố):", non_prime_numbers)


# Hàm chính để thực thi chương trình
def main():
    array = input_numbers()
    process_and_display(array)


if __name__ == "__main__":
    main()
