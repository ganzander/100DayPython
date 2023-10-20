import random

rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

rps = [rock, paper, scissor]
num = random.randint(0, 2)
rpsNum = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
)
print("You Chose :")
print(rps[rpsNum])
print("Computer Chose :")
print(rps[num])

if num == rpsNum:
    print("Draw")
else:
    if rpsNum == 1 and num == 0:
        print("You Won")
    elif rpsNum == 0 and num == 1:
        print("Computer Won")
    elif rpsNum == 2 and num == 1:
        print("You Won")
    elif rpsNum == 1 and num == 2:
        print("Computer Won")
    elif rpsNum == 0 and num == 2:
        print("You Won")
    elif rpsNum == 2 and num == 0:
        print("Computer Won")
