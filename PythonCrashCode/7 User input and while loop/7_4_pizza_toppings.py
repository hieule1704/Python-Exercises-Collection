toppings = set({})
# while True:
#     topping = input("Enter topping name, otherwise enter 'quit' to stop: ")
#     if topping != "quit":
#         toppings.add(topping)
#     else:
#         break
message = ""
while message != 'quit':
    message = input("Enter topping name, otherwise enter 'quit' to stop: ")
    toppings.add(message)
toppings.remove("quit")
for topping in toppings:
    print(f"You will add {topping} to your pizza.")
