import random
minValue = 1
maxValue = 10
randomValue = random.randint(minValue, maxValue)
# update values here if changes needed
userGuess = 'wrong'
while userGuess == 'wrong':
    attempt = input(
        f"Guess the number I'm thinking of between {minValue} and {maxValue}: ")
    try:
        # make sure user input is a number
        number = int(attempt)
        if number == randomValue:
            print("Wow! You're a genius!")
            # to break out of the code
            userGuess = 'right'
        elif number > randomValue:
            # indication to let user know how wrong, and go lower
            print("No, go lower. Guess again")
        else:
            print("No, go higher. Guess again")
    except ValueError:
        print("Please enter a number!")
