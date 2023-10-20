import random


def listToString(s):
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    return str1


stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

print(
    """   
 _                                          
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     """
)

word_list = ["ardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

lives = 6
lost = False

display = []
for letter in chosen_word:
    display.append("_")

# print(listToString(display))
# print(stages[6])

while "_" in display:
    found = False

    if lives == 6:
        print(stages[6])
    elif lives == 5:
        print(stages[5])
    elif lives == 4:
        print(stages[4])
    elif lives == 3:
        print(stages[3])
    elif lives == 2:
        print(stages[2])
    elif lives == 1:
        print(stages[1])
    print(listToString(display))
    guess = input("Guess a letter: ")
    guess = guess.lower()

    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            found = True

    if found == False:
        lives = lives - 1
        print(
            f"Psst you guessed {guess}, that's not in the word. You have lost a life "
        )

    # print(listToString(display))
    if lives == 0:
        print(stages[0])
        print("You lost")
        print("The word was " + chosen_word)
        lost = True

    if "_" not in display:
        print("You Won")
        print("The word was " + chosen_word)
        display = []

    if lost == True:
        display = []
