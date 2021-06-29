#Simple Python Program Number 3 - Number Guessing Game
#Importing Random Module
import random
number = random.randint(1,100)

#First Input
print("Welcome to the Number Guessing Game!")
guess = int(input("Guess a number between 1 and 100: "))
game_end = False

#Game Setup
while game_end != True:
    if guess < number:
        print("The Number you Entered is Lower than the Prize Number")
        guess = int(input("Guess Again: "))
    elif guess > number:
        print("The Number you Entered is Higher than the Prize Number")
        guess = int(input("Guess Again: "))    
    elif guess == number:
        print(f"You Got it! The Prize Number was {number}")
        game_end = True
#End of Program        