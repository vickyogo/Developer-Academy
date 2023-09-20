# Assignment 3: Mad Lib Ibiza

# Concepts to keep in mind:
"""
Strings 
Variables 
Concatenation 
Print Deliverables
"""

# Declare inputs
"""
verb : went
adverb: pleasantly
noun: landscape
adjective: balmy
dj: Black Coffee
temperature (°C): 30
verb: create
"""
##########################################################################################

# 4 Implement the Code

# VERSION 1
"""
Our Mad Lib project incorporate the following data type and methods:
list
strings
Variables
concatenation
f-string for print
for loop
"""
# story
# I travelled to Ibiza by plane.
# The moment I arrived, I was pleasantly surprised by the vibrant scenery that took my breath away.
# The weather is usually sunny, perfect for dancing at the cool beach parties.
# The temperature often reaches around 30°C, making it even more enjoyable.
# At times, you even get the chance to see top DJs such as Black Coffee, or Kerri Chandler live on a set.
# It's the perfect place to unwind and ... cool memories.

# greeting message
print("Welcome to Ibiza Mad Lib story")
print()

# Let's set the variables
transport_mode = input("Enter a mode of transport mode: ").strip().lower()
surprise_adverb = input("Enter an adverb of surprise: ").strip().lower()
Abstract_noun = input("Enter a positive abstract noun: ").strip().lower()
weatherAdj = input(
    "Enter your ideal weather adjective like snowy, sunny etc: ").strip().lower()
favourite_dj = input("Name your favourite DJ: ").strip().lower()
weather_temperature = input(
    "Enter your ideal weather temperature (°C): ").strip().lower()
return_verb = input(
    "Enter a verb for your chosen mode of transport eg fly, drive, ride etc  : ").strip().lower()

# split the tasks line by line to isolate potential issues. Note line_2 has a f-string instead
# of concatenate.

line_1 = "I travelled to Ibiza by " + transport_mode + \
    "," + "it was a beautiful and streefree ride."
line_2 = f"The moment I arrived, I was {surprise_adverb} surprised by the vibrant {Abstract_noun} and calmness that took my breath away. "
line_3 = "The weather is usually " + weatherAdj + \
    ", perfect for dancing at the cool beach parties. "
line_4 = "The temperature often reaches around " + \
    weather_temperature + "°C, making it even more enjoyable. "
line_5 = "At times, you even get the chance to see top DJs such as " + \
    Dj + ", or Kerri Chandler live on a set. "
line_6 = "It's the perfect place to unwind and create memories. I'll definitely " + \
    return_verb + " back again. "


# Time to print the lines altogether
"""print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(line_6)"""

Ibiza_mad_lib = [line_1, line_2, line_3, line_4, line_5, line_6]

for x in Ibiza_mad_lib:
    print(x)
print()  # will create an empty line

print("Thank you for playing with us! For any question about our Ibiza Mad Lib project please do not hesitate.")


# 5 Test
"""
Was fine
improvement ideas: loop to repeat the exercise, isdigit for the temperature, print all lines together
"""


playAgain = input("Do you want to play again? yes or no: \n")

if playAgain.lower() == 'y' or yes:
    print("Game on!")
    continue

else:
    print("You cut your story short, Farewell")
    break
