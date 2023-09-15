import random


greeting = print("Welcome to the special guessing game!")

my_number = random.randint(1, 100)

guess_number = (input("choose your lucky number from 1 to 100 \n"))
print(guess_number)
print(my_number)
number = int(guess_number)
gap_diff = int(my_number) - (number)

if guess_number == my_number:
    print("You're a genius, keep it up!")
elif guess_number < my_number:
    print("too low, better luck next time")
elif guess_number > my_number:
    print("you've gone too far, better luck next time")
