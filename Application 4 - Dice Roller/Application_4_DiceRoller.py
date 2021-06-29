#Python Program Number 4 - Dice Roller
#Importing Random
import random

#Start
print("Welcome to a Dice Roller!")
roll = (input("Type 'Roll' to roll!\n")).lower()
game_end = False
dice_one = '''
 '     '
 '  o  '
 '     '
 '''
dice_two = '''
 '   o '
 '     '
 ' o   '
 '''
dice_three = '''
 ' o   '
 '  o  '
 '   o '
 '''
dice_four = '''
 'o   o'
 '     '
 'o   o'
 '''
dice_five = '''
 'o   o'
 '  o  '
 'o   o'
 '''
dice_six = '''
 'o   o'
 'o   o'
 'o   o'
 '''


#Function
while game_end != True:
    dice = random.randint(1,6)
    if dice == 1:
        print(dice_one)
        print("You Rolled a 1")
    elif dice == 2:
        print(dice_two)
        print("You Rolled a 2") 
    if dice == 3:
        print(dice_three)
        print("You Rolled a 3")
    elif dice == 4:
        print(dice_four)
        print("You Rolled a 4") 
    if dice == 5:
        print(dice_five)
        print("You Rolled a 5")
    elif dice == 6:
        print(dice_six)
        print("You Rolled a 6")
    decision = (input("Type 'Roll' to Roll again or Type 'Stop' if you are Finished.\n")).lower()
    if decision == "roll":
        continue   
    elif decision == "stop":
        print("Goodbye!")
        game_end = True
    else:
        print("You typed Something Different, Game Ends and Goodbye!")
        game_end = True                    
#End of Program        