#3-1
friend_names = ["Duyên","Huỳnh","Hưng","Hảo","Khang"]
for x in friend_names:
    print(x)
x = 0
#3-2
while(x!=len(friend_names)):
    message = "Hello {name}!"
    print(message.format(name=friend_names[x].title()))
    x+=1
