import random

letter = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = [
    "~",
    ":",
    "'",
    "+",
    "@",
    "^",
    "%",
    "-",
    '"',
    "*",
    "|",
    ",",
    "&",
    "<",
    "`",
    ".",
    "_",
    "=",
    "!",
    ">",
    ";",
    "?",
    "#",
    "$",
    "/",
]
password = ""
nr_letter = int(input("Enter the number of letter: "))
nr_numbers = int(input("Enter the number of numbers: "))
nr_symbols = int(input("Enter the number of symbols: "))

for i in range(0, nr_letter):
    x = random.randint(0, nr_letter)
    password += letter[x]
for i in range(0, nr_numbers):
    x = random.randint(0, nr_numbers)
    password += str(numbers[x])
for i in range(0, nr_symbols):
    x = random.randint(0, nr_symbols)
    password += symbols[x]

print("Your password is (easy level) : " + password)

password_shuffled = "".join(random.sample(password, len(password)))
print("Your password is (hard level) : " + password_shuffled)
