# 6 ROOMS
# Define the rooms in the game
game_description = "WELCOME TO IBIZA ADVENTURE ISLAND.\nYou have found 3 gems on the beach and are being chased down by aliens.\nTo hide, you've entered a building but have noticed the aliens have\nfound you and are running your way. Theres no escape through the front door.\nYou must now escape through the back entrance! "
print()
print(game_description)
rooms = ["You are in a room with a door to north and south.",
         "You are in a room with a door to the east and west.",
         "You are in a room with a door to the south, east and west.",
         "You are in a room with a door to the north and east.",
         "You are in a room with a door to the south and west.",
         "You are in a room with a door to the north and south.",
         "You're a genius, you've found the only escape."]
# Set the player's current position
current_room = 0
number_of_gems = 3
print()
print("Current Room: ", current_room)
# Start the game loop
while True:
    if number_of_gems == 0:
        print("YOU'VE BEEN CAUGHT and lost your gems.")
        break
    # Display the description of the current room
    print(rooms[current_room])
    print()
    # Get the player's input
    direction = input(
        "Which direction do you want to go? (north, south, east, west)> ")
    # Check if the player wants to move in a valid direction
    if direction == "north":
        if current_room == 0 or current_room == 3 or current_room == 5:
            current_room += 1
            print("Current Room: ", current_room)
        else:
            print("You can't go north from here, watch your back!")
    elif direction == "south":
        if current_room == 2 or current_room == 4 or current_room == 5:
            current_room -= 1
            print("Current Room: ", current_room)
            number_of_gems -= 1
            print("Number of lives remaining: ", number_of_gems)
        elif current_room == 0:
            print("YOU LOSE! BETTER LUCK NEXT TIME!")
            break
        else:
            print("You can't go south from here, keep your eyes open")
    elif direction == "east":
        if current_room == 1 or current_room == 2 or current_room == 3:
            current_room -= 1
            print("Current Room: ", current_room)
            number_of_gems -= 1
            print("Number of lives remaining: ", number_of_gems)
        else:
            print("You can't go east from here, look out!")
    elif direction == "west":
        if current_room == 2 or current_room == 4 or current_room == 1:
            current_room += 1
            print("Current Room: ", current_room)
        else:
            print("You can't go west from here, you better follow the map!")
    else:
        print("!!! USE YOUR BRAINS !!! YOU CAN'T GO THIS WAY")
    # Check if the player has won the game
    if current_room == 6:
        print(rooms[current_room])
        print(
            f"You made it with a total of {number_of_gems} gems remaining and sold it for £{number_of_gems} billion!! (Monopoly Cash)")
        break
