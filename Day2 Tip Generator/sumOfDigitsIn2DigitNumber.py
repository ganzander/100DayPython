two_digit_number = int(input("Enter any two digit number: "))
onesDigit = two_digit_number%10
twosDigit = two_digit_number//10
print("Sum of digits: "+str(onesDigit+twosDigit))