print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if(size == "L"):
  bill += 25
  if(add_pepperoni == "Y"):
    bill+=3
elif(size == "M"):
  bill += 20
  if(add_pepperoni == "Y"):
    bill+=3
elif(size == "S"):
  bill += 15
  if(add_pepperoni == "Y"):
    bill+=2

if(extra_cheese =="Y"):
  bill+=1
  
print("Your final bill is: $"+str(bill)+".")