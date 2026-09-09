number1 = int(input("Enter a number...."))

number2 = int(input("Enter a number...."))

while number2 !=0:

    rem = number1 % number2

    number1=number2

    number2=rem

print(f"GCD= {number1}")