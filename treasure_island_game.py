print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n") 
#SYNOPSIS-
print("you are on a ship but suddenly a storm struck your ship ,you save your life by jumping on to a rescue boat.The waves swept the boat on to an island.\n")
scene_1=input("\nQ1--Go to island: yes/no\n")
if scene_1=='yes':
  print("you arrive on the island \n")
  scene_2=input('\nQ2--There are three ways: choose-1\n "left/middle/right\n"')
  if scene_2=='left':
   print("You found a treasure chest\n")
   scene_3=input("\nQ3--Search for the key: \n yes/no \n")
   if scene_3=='yes':
     print("you find the key.You open the box and found a piece of old paper with 3563 written on it.you move forward\n")
     scene_4= input("\nQ4--you found a old door saying:\n enter 4 digit passcode to enter\n")
     if scene_4=='3563':
       print("The old door got opened.\n")
       scene_5=input('You have woken up the cursed mummy from its slumber.\n YOU DIED\n RIP+\GAME-OVER') 
     else:
       print("WRONG PASSWORD\n A poison gas released from the lock. you die.\n RIP+ \n GAME-OVER.")
   elif scene_3=='no':
     print("you move forward and found a door.which is locked and you need password to open it.you wander around forest aimlessly and got eaten by a tiger.\nRIP\nGAME-OVER")
  elif scene_2=='right':
   print("You step on a poisonous snake tail and it bite you and you die.\nRIP+\n GAME-OVER ")
  elif scene_2=='middle':
    print("you found a wounded soldier.")
    scene_3=input("\nQ3--He is asking for help. help-him:\n yes/no \n ")
    if scene_3=='yes':
      print("he is thankful for your help,and offer to accompany you on your journey.")
      scene_4=input("\nQ4--With your partner you start your journey again.You found a 2-way route: \nchoose: left/right\n")
      if scene_4=='left':
        print("you both found a cave.")
        scene_5=input('\nQ5--you enter inside the cave . On left side you see a monster sleeping.\n On right side you see an empty room with a box in the corner.\n choose: \n right/left\n')
        if scene_5=='left':
          print(f'you fought with the monster and defeat it with the help of soldier,but soldier died in process.                      YOU WON \n  YOU FOUND THE TREASURE')  
          	
          print("\033[1;32;40m Bright Green  \n")
          print('''
       *********************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')                
          print(''' /^^^^^^^^^^^^^^^^^\           /(|            
                   | ....        ..... |         (  :
                   |  $$           $$  |        __\  \  _____
                   |  ^            ^   |       (____)  `|
                   |       ///////     |      (____)|   |
                   |        ----       |       (____).__|
                    \_________________/         (___)__.|_____
                            ||                 __  __  _____  _    _
                   ________/  \__________      \\  //  || ||  ||   ||
                 /         \__/           \     \\//   || ||  ||   ||
                /  /|      |  |        |\  \     ||    ||_||  ||___||
               /  / |      |  | |....| | \  \    ||    |___|  |_____|
              /  /  |      |  | |____| |  \  \
             /  /   |      |  |        |   \  \
            /  /    |       \/         |    \  \   __                 ____       
                     \________________/             \\            //  || || ||\\   ||
                      |_______________|              \\    /\\   //   || || || \\  ||
                      /                \              \\__//\\__//    ||_|| ||  \\ ||
                     /                  \              \__/  \\_/     |___| ||   \\||
                    /      /_______\     \
                   /      /         \     \
                  /      /           \     \
                 /      /             \     \
                /      /               \     \
               /      /                 \     \  ''')                                        
        elif scene_5=='right':
          print('It was a trap room . you died.\n RIP+ \nGAME-OVER ')
      if scene_4=='right':
        print("you found an old door after opening ,you have woken up the cursed mummy from its slumber.\n YOU DIED\n RIP+\GAME-OVER")
    elif scene_3=='no':
      print('the soldier is suffering from a communicable diease. you also got affected and died after him.\n RIP+\n GAME-OVER')
else:
  print("your boat got sinked & you died.\nRIP+\nGAME-OVER")
