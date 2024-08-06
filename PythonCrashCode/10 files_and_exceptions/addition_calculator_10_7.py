number1=number2=0
while True:
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
    except ValueError:
        print("Input value is not int! You should enter number instead text")
    else:
        result = number1+number2
        print(number1,'+',number2,'=',result)
        message = input("Enter 'q' to quit if you don't want to continue otherwise enter a random character: ")
        if(message.lower()=='q'):
            break
