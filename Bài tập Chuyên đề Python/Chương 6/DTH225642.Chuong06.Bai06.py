# Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU

import random

def create_unique_list(n):
    list = []
    for i in range(n):
        while True:
            ran = random.randint(1, 100)
            if ran not in list:
                list.append(ran)
                break
    return list

def main():
    random_unique_list = create_unique_list(20)
    print(random_unique_list)

if __name__ == '__main__':
    main()