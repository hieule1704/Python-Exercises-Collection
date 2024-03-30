guest_dinner = ["Ngoc Tram","Trang Anh","Thi Dieu","Thi Ven"]
message = "Will {0} go to dinner with me?"
#3-4
#for x in guest_dinner:
#    print(message.format(x.title()))
#3-5
guest_cant = "Ngoc Tram"
guest_dinner.remove(guest_cant)
guest_dinner.append("New Guest")
print(guest_dinner)
#3-6
print("Found bigger table!")
guest_dinner.insert(0,"NewAtFirst")
guest_dinner.insert((len(guest_dinner)//2),"MidGuest")
guest_dinner.append("EndGuest")
print(guest_dinner)
#3-7
print("Can only invite two people for dinner!")
while(len(guest_dinner)>2):
    print(f"Sorry for not invite you {guest_dinner.pop()}")
print("Who still in the list: ",guest_dinner)
del guest_dinner[1]
del guest_dinner[0]
print(guest_dinner)