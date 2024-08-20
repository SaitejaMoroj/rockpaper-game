import random

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

game_images=[rock,paper,scissors]
user=int(input("enter 1 for rock ,2 for paper and 3 for scissors"))
print(game_images[user])
computer_choice=random.randint(0,2)
print(game_images[computer_choice])
if user==1 and computer_choice==2:
    print('user win')
elif user==2 and computer_choice==1:
    print('computer won')
elif(user==3) and (computer_choice==2):
    print("user win")
else:
    print("draw")