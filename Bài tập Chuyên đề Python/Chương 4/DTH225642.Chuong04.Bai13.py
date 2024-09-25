def check_is_perfect_number(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum == num

def check_abundant_number(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum > num

# Main
num = int(input("Nhập số cần kiểm tra: "))
if check_is_perfect_number(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

if check_abundant_number(num):
    print(f"{num} is an abundant number")
else:
    print(f"{num} is not an abundant number")
