# File: CS112_A1_T2_3_20230427.py
# Purpose: A game where two players take turns subtracting perfect square numbers from a starting total until it reaches zero.
# Author: Mohab Hamdy Saleh Mustafa
# ID: 20230427

import math
import random

# Function to check if a number is a square
def is_square(p1):
    number = int(p1)
    square_root = int(math.sqrt(p1)) 
    return square_root * square_root == p1  # Check if the square of the square root equals to the number
  
def is_square(p2):
  number = int(p2)
  square_root = int(math.sqrt(p2)) 
  return square_root * square_root == p2
x = 0 

while True:
  while True:
    # Prompt the user to choose between inputting a number or letting the computer choose a random number
    user_choice = input("""Please enter a choice to start *_*substracting square game*_* :
1. input a number
2. let the computer choose a random number
3. exit the game
""")
    if user_choice == "2":
        # Generate a random number between 10 and 1000 and add it to x
        r_num = random.randint(10, 1000)
        x = x + r_num
        print("The random number is " + str(r_num))
        break
    elif user_choice == "1":
        # Take input from the user and add it to x
        y = int(input("Please enter a number: "))
        x = x + y
        break
    elif user_choice == "3":
        # Exit the game
        print("Thank you for playing!")
        exit()
    else:
        print("Please enter a valid number")  # Prompt the user to enter a valid choice

# Loop to handle the game turns
  while True:
    # Player 1's turn
    p1 = input("The 1st player, please enter a non-zero square number between 1 to " + str(x) + ": ")
    try :
      p1 = int(p1)
      if is_square(p1) and p1 <= x and p1 > 0 :
        x = x - p1
        print("The number is " + str(x))
      else:
        print("Please enter a valid number")
        continue
     
    except ValueError :
        print("Please enter a valid number")  
        continue    
 
 
    if x == 0:
        print("The 1st player wins")  
        break 

    # Player 2's turn (similar logic as Player 1's turn)
    p2 = input("The 2st player, please enter a non-zero square number between 1 to " + str(x) + ": ")
    try :
      p2 = int(p2)
      if is_square(p2) and p2 <= x and p2 > 0 :
        x = x - p2
        print("The number is " + str(x))
      else:
        print("Please enter a valid number")
        continue
    except ValueError :
        print("Please enter a valid number")  
        continue
   
    if x == 0:
        print("The 2st player wins")  
        break
# check if the user wants to play again 
  while True :  
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == 'yes':
      break
    if choice.lower() == 'no' :
      print("Thank you for playing!")
      exit()
    else:
      print("Please enter a valid choice")
      continue
