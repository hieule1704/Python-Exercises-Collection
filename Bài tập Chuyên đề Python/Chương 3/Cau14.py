a = 0
flag = 0
while a < 100:
    b = 0
    while b < 40:
        if (a+b) % 2 == 0:
            print("*",end='')
            flag += 1
        b = b + 1
    print()
    a = a + 1
print(flag)