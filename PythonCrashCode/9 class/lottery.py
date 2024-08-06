import random

def lottery():
    series = (0,1,2,3,4,5,6,7,8,9)

    lottery = []
    for i in range(6):
        lottery.append(random.choice(series))
    return lottery

#Main
my_ticket = (1,7,0,4,0,4)

num_draws = 0
while True:
    num_draws += 1
    my_ticket = lottery()
    draw_ticket = lottery()
    if set(my_ticket) == set(draw_ticket):
        break

# Print the number of draws it took to win
print(f"It took {num_draws} draws to win the lottery!")