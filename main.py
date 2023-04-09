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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
rand_num = random.randint(0, 2)
if rand_num == 0:
  if choice == 1:
    print(f"""the computer             
      {rock}you{paper}          """)
    print("you win")
  elif choice == 2:
    print(f"""the computer            
      {rock}you{scissors}          """)
    print("you lose")
  else :
    print(f"""the computer         
      {rock}you{rock}          """)
    print("null, play again!")
elif rand_num == 1:
  if choice == 0:
    print(f"""the computer              
      {paper}you{rock}          """)
    print("you lose!")
  elif choice == 2:
    print(f"""the computer             
      {paper}you{scissors}          """)
    print("you win")
  else :
    print(f"""the computer              
      {paper}you{paper}          """)
    print("null, play again!")
else:
  if choice == 0:
    print(f"""the computer              
      {scissors}you{rock}          """)
    print("you win!")
  elif choice == 1:
    print(f"""the computer              
      {scissors}you{paper}          """)
    print("you lose!")
  else :
    print(f"""the computer              
      {scissors}you{scissors}          """)
    print("null, play again!")