number = int(input("Enter a number"))

while number !=0:
    last_digit = number%10

    print(last_digit)
    number = number //10