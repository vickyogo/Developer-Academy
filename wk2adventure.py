# CREATED BY: TIDIANE DIALLO, VICTORIA CHIME and SAQIF KHAN
# 6 ROOMS
# Define the rooms in the game
game_intro = "WELCOME TO IBIZA ADVENTURE ISLAND."
game_description = "You have found 5 extraterrestrial Gems on the beach and are being chased down by aliens.\nTo hide, you've entered a building but have noticed the aliens have\nspotted you. There's no escape through the front door.\nYou must now escape through the back door! "
game_instructions = "These 5 gems are extremely valuable, escape and you're sorted for life.\nFind the correct path to the exit. Be careful, if you choose a path leading back to the previous room\n you lose a gem. Lose all 5 gems and it's game over! Good luck.\nYou're going to need it :)"
print(game_intro)
print(game_description)
print()
print(game_instructions)
rooms = ["You are in a room with a door to the north and south.",
         "You are in a room with a door to the east and west.",
         "You are in a room with a door to the south, east and west.",
         "You are in a room with a door to the north and east.",
         "You are in a room with a door to the south and west.",
         "You are in a room with a door to the north and south.",
         "You're a genius, you've found the only escape."]
# Set the player's current position
current_room = 0
number_of_gems = 5
print()
print("Current Room: ", current_room)
# Start the game loop
while True:
    if number_of_gems == 0:
        print("YOU'VE LOST ALL OF YOUR GEMS. GAME OVER!")
        break
    # Display the description of the current room
    print(rooms[current_room])
    print()
    # Get the player's input
    direction_input = input(
        "Which direction do you want to go? (north, south, east, west)> .")
    direction = direction_input.lower()
    # Check if the player wants to move in a valid direction
    if direction == "north":
        if current_room == 0 or current_room == 3:
            current_room += 1
            print("Current Room: ", current_room)
            print("You have proceeded to the next room!")
        elif current_room == 5:
            current_room -= 1
            print("Current Room: ", current_room)
            print("Oh no! You've returned to the previous room, losing one gem!")
            number_of_gems -= 1
            print("Number of gems remaining: ", number_of_gems)
        else:
            print("You can't go north from here, watch your back!")
    elif direction == "south":
        if current_room == 2 or current_room == 4:
            current_room -= 1
            print("Current Room: ", current_room)
            print("Oh no! You've returned to the previous room, losing one gem!")
            number_of_gems -= 1
            print("Number of gems remaining: ", number_of_gems)
        elif current_room == 5:
            current_room += 1
            print("Current Room: ", current_room)
        elif current_room == 0:
            print("GAME OVER! YOU WENT THROUGH THE FRONT DOOR!")
            break
        else:
            print("You can't go south from here, keep your eyes open!")
    elif direction == "east":
        if current_room == 2:
            current_room -= 1
            print("Current Room: ", current_room)
            print("Oh no! You've returned to the previous room, losing one gem!")
            number_of_gems -= 1
            print("Number of gems remaining: ", number_of_gems)
        elif current_room == 3 or current_room == 1:
            current_room += 1
            print("Current Room: ", current_room)
            print("You have proceeded to the next room!")
        else:
            print("You can't go east from here, LOOK OUT!")
    elif direction == "west":
        if current_room == 2 or current_room == 4:
            current_room += 1
            print("Current Room: ", current_room)
            print("You have proceeded to the next room!")
        elif current_room == 1:
            current_room -= 1
            print("Current Room: ", current_room)
            print("Oh no! You've returned to the previous room, losing one gem!")
            number_of_gems -= 1
            print("Number of gems remaining: ", number_of_gems)
        else:
            print("You can't go west from here, you better follow the map!")
    else:
        print("!!! USE YOUR BRAINS !!! YOU CAN'T GO THIS WAY")
    # Check if the player has won the game
    if current_room == 6:
        print(rooms[current_room])
        print(f"You made it with a total of {number_of_gems} gems remaining.")
        print()
        print("Time to trade in your gems.")
        break
# Prizes
if number_of_gems != 0:
    total_prize = []
    print("Trading gems...")
    while True:
        if number_of_gems == 0:
            print("You've used up all of your gems!")
            break
        import random
        play = input("Press ENTER to earn your prizes")
        prizes = [5, 5, 5, 5, 5, 10, 20, 50, 100,
                  100, 100, 100, 500, 500, 500, 1000, 10000]
        # chooses random prizes from the list and sums it up for the gems
        if play == "":
            if number_of_gems > 0:
                prize = random.choice(prizes)
                print(f"£{prize}")
                number_of_gems -= 1
                total_prize += [prize]
                print("Number of gems remaining: ", number_of_gems)
            else:
                break
    total = sum(total_prize)
    print()
    print(f"Amazing, you've won a total of £{total}!")
    print("Disclaimer: To collect your prize, please contact Abayomi. Thank you for playing.")
