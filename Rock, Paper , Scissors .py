print("lets play rock paper scissor")

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

#Write your code below this line 👇


import random

game_image = ["rocks,paper,scissors"]

user_choise = int(input("what do you choose? type 0 for rocks, 1 for paper or 2 for scissors\n."))

if user_choise == 0:
  print(rock)
elif user_choise == 1:
  print(paper)
elif user_choise == 2:
  print(scissors)
else :
  print("you have entered an invalid number")
print("computer chose:")
computer_choise = random.randint(0,2)

if computer_choise == 0:
  print(rock)
elif computer_choise == 1:
  print(paper)
elif computer_choise == 2:
  print(scissors)
else:
  print("you have enter a invalide number")
  
if user_choise == 0 and computer_choise == 2:
  print("you win")
elif user_choise == 2 and computer_choise == 1:
  print("you win")
elif user_choise == 1 and computer_choise == 0:
  print("you win")
elif user_choise == computer_choise:
  print("its a draw")
else:
  print("you loss")
