#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
print(logo)

import random
a=random.randint(0,100)
level=input("Choose a dificulty level, 'easy' or 'Hard'")
life=0
if level=="easy":
    life=10
elif level=="hard":
    life=5
else:
    print("Wrong input.")
i=0
user_value=0
while i<life and user_value!=a:
    user_value=int(input("Make a guess: "))
    if user_value==a:
        print ("You have guessed exact number")
    elif user_value>a:
        print("Too High")
        print("Guess Again!")
    elif user_value<a:
        print("Too Low")
        print("Guess Again!")
    i+=1
    if user_value!=a:
        remaining=life-i
        print(f"You have {remaining} attempts remaining.")
    if life==0:
        print("You Lose")
        
    