import random

#Write your code below this line 👇

options = ['rock','paper','scissors']
user_choice = input('What is your choice? rock - paper - scissors ? ').lower()
computer_choice = random.choice(options)

print(f'User chose {user_choice} -- Computer chose {computer_choice}')

if user_choice == 'rock' and computer_choice == 'rock':
  print('No one won -- stale mate')
if user_choice == 'rock' and computer_choice == 'paper':
  print('Computer won! paper beats rock')
if user_choice == 'rock' and computer_choice == 'scissors':
  print('User won! rock beats scissors')

if user_choice == 'paper' and computer_choice == 'paper':
  print('No one won -- stale mate')
if user_choice == 'paper' and computer_choice == 'scissors':
  print('Computer won! scissors beats rock')
if user_choice == 'paper' and computer_choice == 'rock':
  print('User won! paper beats rock')

if user_choice == 'scissors' and computer_choice == 'scissors':
  print('No one won -- stale mate')
if user_choice == 'scissors' and computer_choice == 'rock':
  print('Computer won! rock beats scissors')
if user_choice == 'scissors' and computer_choice == 'paper':
  print('User won! scissors beats paper')



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end