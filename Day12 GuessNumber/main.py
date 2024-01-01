import random

print("Welcome to the Number Guessing game.")
print("I'm thinking of a number between 1 and 100.")
difficult = input("Choose the diifculty level (easy or hard): ")
number=random.randint(1, 100)

chances=0
if(difficult=='easy'):
    chances = 10
elif(difficult == 'hard'):
    chances=5

while (chances>0):
    print("You have "+str(chances)+" chances remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if(guess==number):
        print("You guessed the correct number.")
        break
    elif(guess<number):
        print("Too Low.")
        chances=chances-1
    else:
        print("Too High.")
        chances=chances-1

if chances==0:
    print("You lost.The number was "+str(number)+".Better luck next time.")