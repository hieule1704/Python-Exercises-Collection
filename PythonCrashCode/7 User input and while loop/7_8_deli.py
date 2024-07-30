sandwich_orders = ['Tuna', 'Chicken', 'Beef', 'Fish',"pastrami", "pastrami", "pastrami", "pastrami", "pastrami"]
finished_sandwich = []
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:  # Loop until sandwich_orders is empty
    sandwich = sandwich_orders.pop(0)  # Remove the first element
    print(f"I made your {sandwich} sandwich")
    finished_sandwich.append(sandwich)

print("Finished sandwiches: ")
for sandwich in finished_sandwich:
    print(sandwich)
