
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
    print(arrProduct)

if __name__ == '__main__':
    main()