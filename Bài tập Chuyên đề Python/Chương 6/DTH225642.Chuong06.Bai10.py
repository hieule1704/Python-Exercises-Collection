class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def input_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                num = int(input(f"Nhập giá trị cho phần tử tại vị trí {i, j}: "))
                self.matrix[i][j] = num

    def output_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end="  ")
            print()

    def is_same_size(self, matrixB):
        return self.rows == matrixB.rows and self.cols == matrixB.cols

    def plus_matrix(self, matrixB):
        if self.is_same_size(matrixB):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += matrixB.matrix[i][j]
        else:
            print("Kích thước của hai ma trận không giống nhau, không thể thực hiện phép cộng.")

def main():
    num_row_A = int(input("Nhập số dòng của ma trận A: "))
    num_col_A = int(input("Nhập số cột của ma trận A: "))
    A = Matrix(num_row_A, num_col_A)
    A.input_matrix()

    num_row_B = int(input("Nhập số dòng của ma trận B: "))
    num_col_B = int(input("Nhập số cột của ma trận B: "))
    B = Matrix(num_row_B, num_col_B)
    B.input_matrix()

    print("Ma trận A là: ")
    A.output_matrix()

    print("Ma trận B là: ")
    B.output_matrix()

    print("Kết quả phép cộng ma trận A + B:")
    A.plus_matrix(B)
    A.output_matrix()

if __name__ == "__main__":
    main()
