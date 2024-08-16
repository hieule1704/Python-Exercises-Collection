# Xử lý List nhp ngẫu nhiên
import random

def create_random_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(0,100))
    return list

def delete_k_element(list, k):
    while k in list:
        list.remove(k)

def is_symmetric_list(list):
    for i in range(len(list)//2):
        if list[i]!=list[len(list)-i-1]:
            return False

    return True

def main():
    list = create_random_list(10)
    print(list)
    print("Is symmetric list:",is_symmetric_list(list))
    k = int(input("Enter k:"))
    delete_k_element(list, k)
    print(list)

if __name__ == '__main__':
    main()