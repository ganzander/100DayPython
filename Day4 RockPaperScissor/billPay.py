import random

names = [" Michael", " James", " Jones", " Jack"]
x = len(names)
num = random.randint(0, x - 1)
any = names[num].replace(" ", "")
print(f"{any} is going to buy the meal today!")
