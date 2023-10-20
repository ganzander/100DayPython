print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name = name1 + name2
name = name.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

first_digit = t + r + u + e
second_digit = l + o + v + e
love_score = first_digit * 10 + second_digit

if love_score < 10 or love_score > 90:
    print(
        "Your score is " + str(love_score) + ", you go together like coke and mentos."
    )
elif love_score > 40 and love_score < 50:
    print("Your score is " + str(love_score) + ", you are alright together.")
else:
    print("Your score is " + str(love_score) + ".")
