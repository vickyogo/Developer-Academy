## Adv game 3 rooms
# Define the rooms in the game
rooms = ["You are in a room with a door to the north.",
          "You are in a room with a door to the south.",
          "You are in a room with a door to the east."]

# Set the player's current position
current_room = 0

# Start the game loop
while True:

    # Display the description of the current room
    print(rooms[current_room])

    # Get the player's input
    direction = input("Which direction do you want to go? (north, south, east)> ")

    # Check if the player wants to move in a valid direction
    if direction == "north":
        if current_room == 0:
            current_room = 1
        else:
            print("You can't go north from here.")

    elif direction == "south":
        if current_room == 1:
            current_room = 0
        else:
            print("You can't go south from here.")

    elif direction == "east":
        if current_room == 1:
            current_room = 2
        else:
            print("You can't go east from here.")

    else:
        print("Invalid direction.")

    # Check if the player has won the game
    if current_room == 2:
        print("You win!")
        break

######################################################################################
## 6 ROOMS
# Define the rooms in the game
rooms = ["You are in a room with a door to north and south.",
          "You are in a room with a door to the east and west.",
          "You are in a room with a door to the north, south, east, and west.",
          "You are in a room with a door to the north and east.",
          "You are in a room with a door to the south and west.",
          "You are in a room with a door to the north and south."]

# Set the player's current position
current_room = 0

# Start the game loop
while True:

    # Display the description of the current room
    print(rooms[current_room])

    # Get the player's input
    direction = input("Which direction do you want to go? (north, south, east, west)> ")

    # Check if the player wants to move in a valid direction
    if direction == "north":
        if current_room == 0 or current_room == 3 or current_room == 5:
            current_room += 1
        else:
            print("You can't go north from here.")
    elif direction == "south":
        if current_room == 1 or current_room == 4 or current_room == 5:
            current_room -= 1
        else:
            print("You can't go south from here.")
    elif direction == "east":
        if current_room == 1 or current_room == 2 or current_room == 3:
            current_room += 1
        else:
            print("You can't go east from here.")
    elif direction == "west":
        if current_room == 2 or current_room == 4 or current_room == 5:
            current_room -= 1
        else:
            print("You can't go west from here.")
    else:
        print("Invalid direction.")

    # Check if the player has won the game
    if current_room == 5:
        print("You win!")
        break

############################################################################################
## 4 ROOMS
# Define the rooms in the game
rooms = ["You are in a room with a door to the north, south, east, and west.",
          "You are in a room with a door to the north and south.",
          "You are in a room with a door to the east and west.",
          "You are in a room with a door to the north, east, and west."]

# Set the player's current position
current_room = 0

# Start the game loop
while True:

    # Display the description of the current room
    print(rooms[current_room])

    # Get the player's input
    direction = input("Which direction do you want to go? (north, south, east, west)> ")

    # Check if the player wants to move in a valid direction
    if direction == "north":
        if current_room == 0 or current_room == 3:
            current_room += 1
        else:
            print("You can't go north from here.")
    elif direction == "south":
        if current_room == 1 or current_room == 3:
            current_room -= 1
        else:
            print("You can't go south from here.")
    elif direction == "east":
        if current_room == 0 or current_room == 2:
            current_room += 1
        else:
            print("You can't go east from here.")
    elif direction == "west":
        if current_room == 1 or current_room == 2:
            current_room -= 1
        else:
            print("You can't go west from here.")
    else:
        print("Invalid direction.")

    # Check if the player has won the game
    if current_room == 3:
        print("You win!")
        break
