#Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại} và xuất ra file output theo mẫu sau:
# “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”. 
while True :
    print("Nhập tên của bạn: ")
    global ten,tuoi
    ten=str(input())
    print("Nhập tuổi của bạn: ")
    tuoi = int(input())
    if(isinstance(tuoi,int)==True):
        break
    else:
        print("Tên hoặc tuổi bạn vừa nhập không hợp lệ vui lòng nhập lại!")
form = "Vào 20 năm nữa, tuổi của {Ten} sẽ là {TuoiCanTim}"
print(form.format(Ten=ten,TuoiCanTim=tuoi+20))