flag = True
while flag:
    age = input("Enter your age or 'quit' to stop: ")
    if age == 'quit':
        flag = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age >= 3 and age <= 12:
            print("Your ticket cost $10!")
        else:
            print("Your ticket cost $15!")
