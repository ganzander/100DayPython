import os
logo = ('''
         ___________
         \         /
          )_______(
          |"""""""|_.-._,.---------.,_.-._
          |       | | |               | | ''-.
          |       |_| |_             _| |_..-'
          |_______| '-' `'---------'` '-'
          )"""""""(
         /________ \
       .-------------.
      /_______________\
        
''')

print (logo)
again = "yes"
secretBid={}

while again == "yes":
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    secretBid[name]=bid
    again = input("Is there any other bidder. Type 'yes' or 'no': ")
    os.system('cls')



v = list(secretBid.values())
k = list(secretBid.keys())
 
print("The winner is " + k[v.index(max(v))] + " with a bid of " + str(max(v)))
