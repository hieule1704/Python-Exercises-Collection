#Game đoán số
import random

possible_result = list(range(1,101))
result = random.choice(possible_result)

flag = 0
while True:
    if(flag==7):
        print("You out of guess time! Lose game! The correct answer is " + str(result))
        quit = input("Enter 'q' to quit, otherwise enter a random character to continue play: ")
        if quit == 'q':
            break
        else:
            flag = 0
    guess = int(input(f"{flag+1} time: Guess a number from 1 to 100: "))
    if guess == result:
        print(f"You guessed the correct number in {result}")
        quit = input("Enter 'q' to quit, otherwise enter a random character to continue play: ")
        if quit == 'q':
            break
        else:
            flag = 0
    elif guess > result:
        print("Too high!")
        flag+=1
    else:
        print("Too low!")
        flag+=1
