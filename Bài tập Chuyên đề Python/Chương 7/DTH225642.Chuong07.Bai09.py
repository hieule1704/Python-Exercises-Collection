def LuuFile(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def DocFile(path):
    arrdata = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrdata.append(arr)
    file.close()
    return arrdata


def XuatFile(data):
    for row in data:
        for element in row:
            print(element, end='\t')
        print()


def NhapDanhMuc(dsdm):
    madm = input("Nhập mã danh mục: ")
    tendm = input("Nhập tên danh mục: ")
    line = madm + ";" + tendm
    LuuFile(dsdm, line)


def XuatDanhMuc(dsdm):
    print("Danh sách danh mục:")
    for row in dsdm:
        print(f"Mã: {row[0]} - Tên: {row[1]}")


def TimDanhMuc(dsdm, madm):
    for i, row in enumerate(dsdm):
        if row[0] == madm:
            return i
    return -1


def NhapSanPham(dsdm, dssp):
    masp = input("Nhập mã sản phẩm: ")
    tensp = input("Nhập tên sản phẩm: ")
    dongia = float(input("Nhập đơn giá: "))
    madm = input("Nhập mã danh mục: ")

    if not TimDanhMuc(dsdm, madm):
        print(f"Lỗi: Danh mục '{madm}' không tồn tại.")
        return

    line = masp + ";" + tensp + ";" + str(dongia) + ";" + madm
    LuuFile(dssp, line)


def XuatSanPhamTheoDanhMuc(dsdm, dssp):
    for dm in dsdm:
        print(f"> Sản phẩm thuộc danh mục '{dm[0]}': '{dm[1]}'")
        for row in dssp:
            if row[3] == dm[0]:
                print(f"  Mã: {row[0]} - Tên: {row[1]} - Giá: {row[2]} - Danh Mục: {row[3]}")


def TimSanPham(dssp, masp):
    for i, row in enumerate(dssp):
        if row[0] == masp:
            return i
    return -1


def SuaSanPham(dsdm, dssp, path):
    masp = input("Nhập mã sản phẩm cần sửa: ")
    tim_index = TimSanPham(dssp, masp)

    if tim_index == -1:
        print(f"Lỗi: Sản phẩm '{masp}' không tồn tại.")
        return

    print("Mã sản phẩm cần sửa: ", dssp[tim_index][0])
    new_masp = input("Nhập mã sản phẩm mới: ")
    print("Tên sản phẩm cần sửa: ", dssp[tim_index][1])
    new_tensp = input("Nhập tên sản phẩm mới: ")
    print("Giá sản phẩm cần sửa: ", dssp[tim_index][2])
    new_dongia = float(input("Nhập giá sản phẩm mới: "))
    while (1):
        print("Danh mục sản phẩm cần sửa: ", dssp[tim_index][3])
        new_madm = input("Nhập mã danh mục sản phẩm mới: ")
        if TimDanhMuc(dsdm, new_madm) != -1:
            break

    updated_product_data = [new_masp, new_tensp, str(new_dongia), new_madm]
    dssp[tim_index] = updated_product_data

    print("Sửa thành công!")


def main():
    dsdm = "D:\Python\Chuong7\dsdmBai9.txt"
    dssp = "D:\Python\Chuong7\dsspBai9.txt"

    while (1):
        datadm = DocFile(dsdm)
        datasp = DocFile(dssp)
        print("1. Nhập danh mục | 2. Nhập sản phẩm | 3. Xuất danh sách danh mục")
        print("4. Xuất danh sách sảm phẩm theo danh mục")
        print("5. Tìm sản phẩm  | 6. Sửa sản phẩm")
        print("0. Ẽxit")
        otp = int(input("Nhập lựa chọn: "))
        match (otp):
            case 1:
                n = int(input("Nhập số lượng: "))
                for i in range(n):
                    NhapDanhMuc(dsdm)

            case 2:
                if (len(datadm) == 0):
                    print("Chưa có danh mục nào! vui lòng nhập danh mục!")
                else:
                    n = int(input("Nhập số lượng: "))
                    for i in range(n):
                        NhapSanPham(dssp, dsdm)

            case 3:
                if (len(datadm) == 0):
                    print("Chưa có danh mục nào! vui lòng nhập danh mục!")
                else:
                    XuatDanhMuc(datadm)

            case 4:
                XuatSanPhamTheoDanhMuc(datadm, datasp)

            case 5:
                masp = input("Nhập mã sản phẩm cần tìm: ")
                vtri = TimSanPham(datasp, masp)
                if (vtri == -1):
                    print(f"Không tìm thấy sản phẩm {masp}!")
                else:
                    print(
                        f"  Mã: {datasp[vtri][0]} - Tên: {datasp[vtri][1]} - Giá: {datasp[vtri][2]} - Danh Mục: {datasp[vtri][3]}")

            case 6:
                SuaSanPham(datadm, datasp, dssp)

            case __:
                break


if __name__ == "__main__":
    main()