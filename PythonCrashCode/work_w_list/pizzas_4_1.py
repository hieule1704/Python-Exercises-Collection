pizzas = ["Seafood Pizza","Beef Pizza","Chicken Pizza"]
"""for pizza in pizzas:
    print(f"I like {pizza.title()}.")
    print(f"I very love {pizza.title()}!\nI really love pizza@@\n")"""
friend_pizzas = pizzas[:]
pizzas.append("Egg Pizza")
friend_pizzas.append("Fish Pizza")

print("My favorite pizza: ")
for pizza in pizzas:
    print(pizza)
print("My friend favorite pizza: ")
for pizza in friend_pizzas:
    print(pizza)