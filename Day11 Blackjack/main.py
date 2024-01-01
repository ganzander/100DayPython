import random

logo="""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
print("Welcome To The BLACKJACK Game.")
computerCard=[]
playerCard = []

play = input("Do you want to play the game (y (yes) or n (no)): ")
playerCard.append(random.randint(1,13))
playerCard.append(random.randint(1,13))
computerCard.append(random.randint(1,13))
computerCard.append(random.randint(1,13))
playerSum = sum(playerCard)
computerSum = sum(computerCard)

while (play=='y'):
    playerSum = sum(playerCard)
    computerSum = sum(computerCard)
    print("Your cards "+str(playerCard)+". Your final score : "+str(playerSum))
    print("Computer first card : "+str(computerCard[0]))

    if(playerSum>21):
        print("Computer won 😭")
        print("Computer cards "+str(computerCard)+". Computer final score : "+str(computerSum))
        break
    elif(computerSum>21):
        print("Player won 😀")
        print("Computer cards "+str(computerCard)+". Computer final score : "+str(computerSum))
        break

    play = input("Do you want to play the game (y or n): ")
    if(play=='y'):
        playerCard.append(random.randint(1,13))
        computerCard.append(random.randint(1,13))
    else:
        break

if (play=='n'):
    closePlayer=abs(21-playerSum)
    closeComputer=abs(21-computerSum)
    if(closePlayer<=computerSum):
         print("Player won 😀")
         print("Computer cards "+str(computerCard)+". Computer final score : "+str(computerSum))
    else:
        print("Computer won 😭")
        print("Computer cards "+str(computerCard)+". Computer final score : "+str(computerSum))