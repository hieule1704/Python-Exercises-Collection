
def LuuFile(path,data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()
def DocFile(path):
    arrProduct = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct

def OutputData(datalist):
    for row in datalist:
        for element in row:
            print(element, end='\t')
        print()
    print()

def sortData(arrProduct):
    for i in range(len(arrProduct)-1):
        for j in range(i,len(arrProduct)):
            a = arrProduct[i]
            b = arrProduct[j]
            if float(a[2]) > float(b[2]):
                arrProduct[i] = b
                arrProduct[j] = a
def main():
    path = "XuLyFile.txt"
    while True:
        id = input("Enter identification string: ")
        name = input("Enter name: ")
        price = input("Enter price: ")
        product = [id, name, price]
        data = ";".join(product)
        LuuFile(path,data)
        flag = input("Do you want to continue (y/n)")
        if flag == "n":
            break

    arrProduct = DocFile(path)

    # Xuất sản phẩm khi chưa sắp xếp
    OutputData(arrProduct)
    # Sắp xếp giảm giá
    sortData(arrProduct)

    # Xuất sản phẩm sau khi sắp xêếp
    OutputData(arrProduct)

if __name__ == '__main__':
    main()