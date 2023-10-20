target = int(input("Enter a number between 0 and 1000: "))
sum = 0
for i in range(0, target + 1):
    if i % 2 == 0:
        sum = sum + i
print(sum)
