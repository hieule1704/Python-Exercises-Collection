pets = ["Cat","dog","Duck"]
"""for pet in pets:
    print(f"A {pet.lower()} would make a great pet.")
print("Any of these animals would make a great pet!")"""
sub_pets = ["Bird","Fish","Rabbit"]
for sub_pet in sub_pets:
    pets.append(sub_pet)
print("The first three items in the list are:",pets[:3])
print("Three items from the middle of the list are:",pets[1:4])
print("The last three items in the list are:",pets[-3:])