#This Game is Called Scrabble Game
#Who Picks 3 Numbers That Adds up to 15 Wins.
#The Game Displays The List of The Avaliable Numbers Before any Player Picks a Number.
#The Player Should Not pick an Already Picked Number.
#When a Player Picks a Number The Number is Removed so it Can not Be Picked Again.
#When any of The Players Win The Game Will Display Either "Player1 Wins" or "Player2 Wins".
#When None of The Players Win The Game Will Display "Draw".
#If a Player Chooses an Already Removed Number The Game Will Give Them The Chance To Enter Another Number.
#If The Player Wants To Restart The Game There Is a pop-up Message That Will Display The Option.
#If The Player Types "Y" or "y" The Game Will Restart.
#If The Player Types "N" or "n" The Game Will End.

import os
start_trigger = str(input("Please Press Enter To Start The Game."))
print()

def the_start():
 print("Who Picks 3 Numbers That Add Up To 15 Wins:")
 print("------------------------------------------")
 print()

def the_game():
 list_of_num = [1,2,3,4,5,6,7,8,9]
 sum1 = 0
 sum2 = 0
 number_of_turns = 0

 
 for i in range(0,3):
    print("Available Numbers:",list_of_num)

    player1_input = (input("Player1 Turn: " ))

    if player1_input == "":
        while player1_input == "":
            print("*Please Enter a Number Do Not Leave Your Turn Empty*")
            player1_input = input("Player1 Please Enter a Number: ")
            print()

    if player1_input.isalpha():
       while player1_input.isalpha():
          print("* Please Do Not Enter a Word Or a Letter Enter a Number *")
          player1_input = input("Player1 Please Enter an Avaliable Number: ")
          print()
          if player1_input == "":
            while player1_input == "":
              print("* Please Enter a Number Do Not Leave Your Turn Empty *")
              player1_input = input("Player1 Please Enter a Number: ")
              print()
          

    if player1_input.isdigit():
      player1_input = int(player1_input)
      while player1_input not in list_of_num:
          print()
          print("* The Number That Player1 Is Not Available *")
          print("Please Choose a Number From This List: ",list_of_num) 
          player1_input = int(input("Player1 Enter Another Number: "))

  
      list_of_num.remove(player1_input)
     

    player2_input = (input("Player2 Turn: " ))

    if player2_input == "":
        while player2_input == "":
            print("*Please Enter a Number Do Not Leave Your Turn Empty*")
            player2_input = input("Player2 Please Enter a Number: ")


    if player2_input.isalpha():
        while player2_input.isalpha():
            print(" * Please Do Not Enter a Word Or a Letter Enter a Number *")
            player2_input = input("Player2 Please Enter an Avaliable Number: ")
            print()
            if player2_input == "":
              while player2_input == "":
                print("*Please Enter a Number Do Not Leave Your Turn Empty*")
                player2_input = input("Player2 Please Enter a Number: ")

    if player2_input.isdigit():
       player2_input = int(player2_input)
       while player2_input not in list_of_num :
          print()
          print("* The Number That Player2 Choose Has Been Already Picked *")
          print("Please Choose a Number From This List:",list_of_num) 
          player2_input = int(input("Player2 Enter Another Number: "))
             
    list_of_num.remove(player2_input)

            
    number_of_turns += 1
    print()
    
    sum1 = sum1 + player1_input
    sum2 = sum2 + player2_input

    if number_of_turns == 3:
      if sum1 == 15 and sum2 == 15:
          print("-Draw-")
          break
      if sum1 == 15:
       print("-Player1 Wins-")

      if sum2 == 15:
       print("-Player2 Wins-")

    
    
 if sum1 != 15 and sum2 !=15:
      print("-Draw-")
      
while start_trigger != "":
    start_trigger = str(input("The Game Will Not Start Unless You Press Enter."))
    print()
    
if start_trigger == "":
    the_start()
    the_game()
    

print()
restart_trigger = ""

while restart_trigger == "":
 restart_trigger = str(input("Do You Want To Play Again?/(Y/N): "))

 if restart_trigger == "Y" or restart_trigger == "y":
  print()
  os.system('CLS')
  the_game()
  restart_trigger = ""

 if restart_trigger == "N" or restart_trigger == "n":
    print("-Thank You For Playing-")
  

