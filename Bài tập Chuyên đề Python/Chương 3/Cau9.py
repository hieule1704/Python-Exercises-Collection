while True:
    month = int(input("Enter month number: "))
    if month < 1 or month > 12:
        print("Invalid month number! Please enter again")
    else:
        break

if(month in range(1,4)):
    print("Your month is in the first quarter of year!")
elif(month in range(4,7)):
    print("Your month is in the second quarter of year!")
elif(month in range(7,10)):
    print("Your month is in the third quarter of year!")
else:
    print("Your month is the last quarter of year!")