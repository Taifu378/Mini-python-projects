print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
turn = input("Would you like to turn left or right L for left R for right? ")

if turn == "R":
    print("You got attacked by tribesmen. GAME OVER.")
elif turn == "L":
    choice = input("Would you like to swim or wait S to swim W to wait? ")
    if choice == "S":
        print("You got eaten by sharks. GAME OVER.")
    elif choice == "W":
        print("A building with 3 doors has come up.")
        door = input("Pick a door press r for red door b for blue door y for yellow door: ")
        if door == "r":
            print("You activated a trap. GAME OVER.")
        elif door == "b":
            print("You fell into a pit of snakes. GAME OVER.")
        elif door == "y":
            print("WELL DONE YOU FOUND THE TREASURE!!!")
        else:
            print("Invalid letter entered.")
    else:
        print("Invalid letter entered")
else:
    print("Invalid letter entered")