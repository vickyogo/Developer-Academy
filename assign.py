import random

dice_toss = random.randint(1, 6)

greeting = print("Welcome to roll your dice genius")

choice = int(input('choose your favourite number from 1 to 6 \n'))
print(choice)

if choice <= dice_toss:
    print("you nearly made it, go higher with your choice")
elif choice > dice_toss:
    print("your choice is off the roof, try a lower number")
elif choice == dice_toss:
    print("Good job! you're a Genius!")
elif choice == ValueError:
    print("Type a real number")
else:
    print("That is incorrect, try again!")
