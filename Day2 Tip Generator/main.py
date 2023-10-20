print("Welcome to the Tip Generator")
total_bill = float(input("Enter the bill: "))
num_people = int(
    input("Enter the number of people in which the bill has to be split: ")
)
percent = int(input("Enter the tip percent 10, 12 or 15: "))

bill = total_bill + ((total_bill * percent) / 100)
split_bill = bill / num_people
print("Each people have to pay $" + str(split_bill))
