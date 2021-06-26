#Program Number 2 of working Solo
#Game of Rock Paper Scissors

#Setting Up
import random
rock = r'''
  |       | 
 /         \
 |         |
 | |       |
  \|     , |
   |_| |_|-'
     `-'
  '''
paper = """
        .-.
      .-| |-.
      | | | |
      | | | |-.
      | | | | |
      |_|_|_| |
     / )    `-|
    | | `--   |
    |     ||  |
    \     '   /
     |       |
     |       | 
    """
scissors = """
  __      __
 ( _\    /_ )
  \ _\  /_ /
   \ _\/_ /_ _
   |_____/_/ /|
   (  (_)__)J-)
   (  /`.,   /
    \/  ;   /
     | === |
    """

#Start of Game
print("Welcome to the Game of Rock Paper Scissors")
User_Choice = input("Enter 'Rock' 'Paper' or 'Scissors' and Challenge the PC! ").lower()
Cpu_Choice = random.randint(0,2)


#Game Calculations
if User_Choice != 'rock' and User_Choice != 'paper' and User_Choice != 'scissors':
    print('You Entered an Invalid Answer and Lose!')
elif User_Choice == 'rock':
    print(f'You Chose:\n{rock}')
    if Cpu_Choice == 0:
        print(f'The CPU Chose: \n{rock}')
        print('You both Chose the Same Thing and Tied!')
    elif Cpu_Choice ==1:
        print(f'The CPU Chose: \n{paper}')
        print('The CPU Chose Paper and You Lost :(')  
    else:
        print(f'The CPU Chose: \n{scissors}')
        print('The CPU Chose Scissors and You Destroyed Him!')
elif User_Choice == 'paper':
    print(f'You Chose:\n{paper}')
    if Cpu_Choice == 0:
        print(f'The CPU Chose: \n{rock}')
        print('The CPU Chose Rock and You Destroyed Him!')  
    elif Cpu_Choice ==1:
        print(f'The CPU Chose: \n{paper}')
        print('You both Chose the Same Thing and Tied!')  
    else:
        print(f'The CPU Chose: \n{scissors}')  
        print('The CPU Chose Scissors and You Lost :(')
elif User_Choice == 'scissors':
    print(f'You Chose:\n{scissors}')
    if Cpu_Choice == 0:
        print(f'The CPU Chose: \n{rock}')
        print('The CPU Chose Rock and You Lost :(')
    elif Cpu_Choice ==1:
        print(f'The CPU Chose: \n{paper}')
        print('The CPU Chose Paper and You Destroyed Him!')
    else:
        print(f'The CPU Chose: \n{scissors}')
        print('You both Chose the Same Thing and Tied!')
#End of Program                         