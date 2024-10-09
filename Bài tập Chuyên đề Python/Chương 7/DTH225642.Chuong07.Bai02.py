def LuuFile(path,data):
    file=open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()

def DocFile(path):
    arrSo=[]
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        arr=data.split(',')
        arrSo.append(arr)
    file.close()
    return arrSo

def XuatFile(data):
    for row in data:
        for element in row:
            print(element,end='\t')
        print()

def XuatSoAmTrenMoiDong(data):
    for row in data:
        for element in row:
            number=int(element)
            if number<0:
                print(number,end='\t')
        print()


def main():
    dssp="C:\Python\Chuong7\databaseBai2.txt"

    data=DocFile(dssp)

    print("List:")
    XuatFile(data)

    data=DocFile(dssp)

    print("List số âm:")
    XuatSoAmTrenMoiDong(data)



if __name__ == "__main__":
    main()