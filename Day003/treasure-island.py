print(''' **********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("welcome to treasure island")
print("Your mission is to find the find the treasure.")
choise1 = input('You are at a crossover, where do u want to  go first? Type "left" or "right".').lower()
if choise1 == "left":
    choise2 = input('You have come to a lake. there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choise2 == "wait":
        choise3 = input('You arrived at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which colour would you choose?').lower()
        if choise3 == "red":
            print("It is a room full of fire. Game over.")
        elif choise3 == "yellow":
            print("You found the treasure. You win.")
        elif choise3 == "blue":
            print("You enter a room full of poison. Game over.")
        else:
            print("You choose a door that does not exist. Game over.")
    else:
        print("You are attacked by an alligator. Game over.")
else:
    print("You fell into a hole. Game over.")
