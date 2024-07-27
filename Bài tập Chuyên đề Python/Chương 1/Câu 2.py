# Cách của mình
second = int(input("Nhập vào số giây: "))
hour = int(second / 60 / 60)
minute = int((second - hour*60*60) / 60)
second = second % 60
if(hour>12):
    hour = hour - 12
    print(hour,":",minute,":",second,"PM")
else:
    print(hour,":",minute,":",second,"AM")

# Cách trong tài liệu
# t=int(input("Nhập số giây:"))
# hour=(t//3600)%24
# minute=(t%3600)//60
# second=(t%3600)%60
# print(hour,":",minute,":",second)




