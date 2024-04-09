import random

def lottery():
    series = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e')

    lottery = ""
    for i in range(4):
        lottery += str(random.choice(series))
    return lottery
