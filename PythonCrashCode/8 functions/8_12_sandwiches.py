def sandwich_order(*args):
    print("Your sandwich is ready with following topping below!")
    for arg in args:
        print(f"    - {arg}")

toppings = []
while True:
    topping = input("Enter what topping would you like to put into your sandwich?")
    toppings.append(topping)
    flag = input("Do you want more topping? (y/n)")
    if flag.lower() == "n":
        break
sandwich_order(*toppings)