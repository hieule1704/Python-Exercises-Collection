#Nhập số bất kỳ ở hệ thập phân và hiển thị ra ở hệ bát phân.(Có xử lý ngoại lệ đầu vào)
so=input()
try:
    soThapPhan=int(so)
except:
    print("Định dạng số bạn vừa nhập không hợp lệ!")
else:
    # %d dong vai tro giu cho cho 1 gia tri so thap phan
    # %o dong vai tro giu cho cho 1 gia tri so bat phan
    print("Số thập phân %d có giá trị trong hệ bác phân là %o"%(soThapPhan,soThapPhan))
