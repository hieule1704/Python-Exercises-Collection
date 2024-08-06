import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return random.randint(1, self.sides)

#Main
my_die = Die()
for i in range(10):
    print(f"The {i+1}st roll and the result is {my_die.roll_die()}")

print("\n")

die_10side = Die(10)
for i in range(10):
    print(f"The {i+1}st roll and the result is {die_10side.roll_die()}")

print("\n")

die_20side = Die(20)
for i in range(10):
    print(f"The {i+1}st roll and the result is {die_20side.roll_die()}")