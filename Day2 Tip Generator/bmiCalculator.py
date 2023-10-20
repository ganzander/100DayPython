weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = int(weight // (height**2))

print("Your body mass index is: "+str(bmi))