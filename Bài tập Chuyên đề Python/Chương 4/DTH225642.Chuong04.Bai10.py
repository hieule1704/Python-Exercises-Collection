#Vẽ các hình Vuông, tam giác,đồng hồ cát dựa trên chiều cao đã cho
import math, time
def veHinhTamGiac(chieuCao):
    for i in range(1, chieuCao + 1):
        # Dòng có số lượng sao tăng dần từ 1 đến chieuCao
        print('   ' * (chieuCao - i) + '*  ' * i)

def veHinhDongHoCat(chieuCao):
    #Hình đồng hồ cát chỉ nhận chiều cao là số lẻ do tính chất đối xứng 2 bên với trục
    if(chieuCao%2==0):
        chieuCao-=1
    for i in range(1,chieuCao+1):
        #Nữa trên trục đồng ồ
        if i < math.ceil(chieuCao/2):
            #2 dòng đầu tiền, các dấu * liền nhau
            if(i<=2):
                print(i*'*  ')
            #Các dòng còn lại, có khoảng trắng tren giữa
            else:
                print('*  '+(i-2)*'   '+'*  ')
        #Phần trục đối xứng đồng hồ
        elif i == math.ceil(chieuCao/2):
            print(chieuCao*'*  ')
        #Nữa dưới đồng hồ
        else:
            #Hai dòng cuối các dấu * liền nhau
            if(i==chieuCao-1 or i==chieuCao):
                print((i-1)*'   '+'*  '*(chieuCao-i+1))
            # Các dòng còn lại, có khoảng trắng tren giữa
            else:
                print((i-1)*'   '+'*  '+'   '*(chieuCao-i-1)+'*  ')

chieuCao = int(input("Nhập chiều cao cho hình mà bạn muốn vẽ: "))
veHinhTamGiac(chieuCao)
print()
time.sleep(5)
veHinhDongHoCat(chieuCao)