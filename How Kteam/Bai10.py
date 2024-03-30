#Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại} và xuất ra file output theo mẫu sau:
# “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”. 
while True :  #Vòng lặp vô hạn
    print("Nhập tên của bạn: ") 
    global ten,tuoi #Khai báo biến toàn cục
    ten=str(input()) 
    try:
        print("Nhập tuổi của bạn: ") 
        tuoi = int(input()) 
    except:
        print("Tuổi bạn vừa nhập không hợp lệ vui lòng nhập lại!") 
        continue
form = "Vào 20 năm nữa, tuổi của {Ten} sẽ là {TuoiCanTim}" #Khai báo chuỗi form
print(form.format(Ten=ten,TuoiCanTim=tuoi+20)) #In ra màn hình      