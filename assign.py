import random

greeting = print("Welcome to roll your dice genius")
# use random integer, print, while loop
minValue = 1
maxValue = 6

# initialise variable for the while loop
rollagain = 'y'

while rollagain == 'y' or rollagain == 'yes':
    print('Rolling the dice')
    dice_value = random.randint(minValue, maxValue)
    print(f'You rolled a {dice_value}!')

    rollAgain = input("Do you want to try again? Type yes to continue or any other ket to exit: ")
  

print('Thank you for playing!')

# code doesn't
