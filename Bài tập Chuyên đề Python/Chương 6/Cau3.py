# Xử lý List Đa chiều
import random

from numpy import tensordot


def creat_tensor(row, colum):
    list = []
    for i in range(row):
        lst_row = []
        for j in range(colum):
            lst_row.append(random.randint(0,100))
        list.append(lst_row)
    return list

def output_tensor(list, row, colum):
    print("Mảng 2 chiều của bạn là: ")
    for i in range(row):
        for j in range(colum):
            print(list[i][j],end="  ")
        print()

def output_column(list, k):
    i = 0
    while i < len(list):
        print(list[i][k-1])
        i += 1

def output_row(list, k):
    i = 0
    while i < len(list[k-1]):
        print(list[k-1][i], end="  ")
        i += 1
    print()

def find_max(list, num_row, num_colum):
    max = list[0][0]
    for i in range(num_row):
        for j in range(num_colum):
            if list[i][j] > max:
                max = list[i][j]
    return max

def main():
    num_row = int(input("Nhập số dòng của danh sách: "))
    num_colum = int(input("Nhập số cột của danh sách: "))
    tensor_2d = creat_tensor(num_row, num_colum)
    output_tensor(tensor_2d, num_row, num_colum)
    find_col = int(input("Nhập số cột mà bạn muốn in ra màng hình: "))
    output_column(tensor_2d, find_col)
    find_row = int(input("Nhập số dòng mà bạn muốn in ra màng hình: "))
    output_row(tensor_2d, find_row)
    print(f"Gía trị MAX lớn nhất trong list là: {find_max(tensor_2d, num_row, num_colum)}")

if __name__ == '__main__':
    main()