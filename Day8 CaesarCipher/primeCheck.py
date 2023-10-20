def prime_checker(number):
    prime = True
    for i in range(2, int(n**0.5)):
        if number % i == 0:
            prime = False
            break
    return prime


n = int(input("Enter any number: "))

isPrime = prime_checker(number=n)
if isPrime == True:
    print("It's a prime number.")
else:
    print("It's not a prime number.")
