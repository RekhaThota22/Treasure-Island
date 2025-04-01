
print("Welcome to Treasure Island . Your Mission is to find the treasure")
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************)''')

decision = input(f"You are at a cross road . Where do you want to go ? \n Type 'Left or 'right' ").lower()
if decision == 'left' :
   lake = input(f"There is an Island on the middle of the lake. \n Do you want to swim or wait for a boat? \n Type 'swim or 'wait' ").lower()
   if lake == 'wait':
       door = (input(f"You arrive at the Island unharmed \n There ia house with 3 doors .\n "
             f"one red ,one yellow and one blue \n "
             f"which one do you choose\n"))
       if door =='red':
           print(f"Room is full of fire \n GAME OVER")
       elif door =='yellow':
           print(f"You found the treasure \n You Win")
       elif door == 'blue':
           print(f"Room is full of beasts \n GAME OVER")
       else:
           print(f"You choose a dor that doesn't exists \n GAME OVER")

   else :
        print(f"Attacked by trout. \n GAME OVER")
        exit()
else :
    print(f"Fall into a hole. \n GAME OVER")
    exit()
