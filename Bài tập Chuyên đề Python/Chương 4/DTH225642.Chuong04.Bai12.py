#Viết hàm oscillate

def oscillate(star,end):
    oscillate_list = []
    for i in range(star,end):
        oscillate_list.append(i)
        oscillate_list.append(i*(-1))
    return oscillate_list

#Main
for n in oscillate(-3,5):
    print(n, end=' ')
print()