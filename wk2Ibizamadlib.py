# Ibiza Madlibs Generator

while True:
    print("\nWELCOME TO IBIZA MAD LIB STORY")
    print("Game Instructions: Please fill in the blanks.")
    print()  # will create an empty line

    # Let's set variables for all inputs
    transport_mode = input(
        "How did you travel to Ibiza? by... ").strip().lower()
    surprise_adverb = input("Enter an adverb of surprise: ").strip().lower()
    abstract_noun = input(
        "What caught your attention the most at your arrival: the ...").strip().lower()
    weather_adjective = input(
        "Enter your ideal weather adjective like sunny, snowy... ").strip().lower()
    temperature = input("Enter your ideal temperature (°C): ").strip().lower()

    # Let's ensure that a number is entered for the temperature
    while not temperature.isdigit():
        print("Please enter a number instead.")
        temperature = input(
            "Enter your ideal temperature (°C): ").strip().lower()

    dj = input("Name your favourite DJ: ").strip().lower()
    verb = input(
        "A verb for your chosen mode of transport: hint..drive, ride, swim ").strip().lower()

    # Story lines are set as variables and include concatenation as well as f-strings
    line_1 = "I travelled to Ibiza by " + transport_mode + \
        ". It was a beautiful and stress free journey. "
    line_2 = f"The moment I arrived, I was {surprise_adverb} surprised by the vibrant {abstract_noun} and calmness that took my breath away. "
    line_3 = f"The weather is usually {weather_adjective}, perfect for dancing at the amazing beach parties. "
    line_4 = f"The temperature often reaches around {temperature}°C, making it even more enjoyable. "
    line_5 = f"At times, you even get the chance to see top DJs such as {dj}, or Kerri Chandler live on set. "
    line_6 = f"It's the perfect place to unwind and create great memories. I would definitely {verb} back again."

    print("\nNow let's put this altogether!\n")

    # Time to gather all lines together inside a list and print the story
    Ibiza_mad_lib = [line_1, line_2, line_3, line_4, line_5, line_6]

    # A for loop allows each item of the list to be printed
    for x in Ibiza_mad_lib:
        print(x)
    print()

    # Finally, give the user the opportunity to play again
    repeat = input("Do you want to play again? (yes/no) ").strip().lower()
    if repeat != "yes":
        print("\nYou cut your story short. Farewell!")
        print()
        break  # Exit the loop
