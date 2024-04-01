number1=number2=0
while(number1!='q' and number2!='q'):
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
    except ValueError:
        print("Input value is not int! You should enter number instead text")
    else:
        result = number1+number2
        print(number1,'+',number2,'=',result)
        message = input("Do you want to continue(Y/N): ")
        if(message.upper()=='N'):
            break
