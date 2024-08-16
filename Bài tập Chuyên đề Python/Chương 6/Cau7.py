# def input_string():
#     while True:
#         string = input("Nhap day so tang dan: ")
#         value = int(string[0])
#         flag = True
#         for i in range(1,len(string)):
#             if int(string[i]) <= value:
#                 flag = False
#                 break
#             else:
#                 value = int(string[i])
#         if(flag == True):
#             print(string)
#             break
#         else:
#             print("Dãy số bạn vừa nhập không theo thứ tu tang dan vui long nhap lai!")
#
# if __name__ == '__main__':
#     input_string()

def input_sorted_sequence():
    while True:
        try:
            # Nhập dãy số từ người dùng và chuyển thành danh sách các số nguyên
            sequence = list(map(int, input("Nhập một dãy các số theo thứ tự tăng dần"
                                           ", cách nhau bởi khoảng trắng: ").split()))

            # Kiểm tra xem dãy số có theo thứ tự tăng dần hay không
            if all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1)):
                return sequence
            else:
                print("Dãy số không theo thứ tự tăng dần. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng chỉ nhập các số nguyên.")

def main():
    sequence = input_sorted_sequence()
    print("Dãy số đã nhập: ", sequence)

if __name__ == "__main__":
    main()


