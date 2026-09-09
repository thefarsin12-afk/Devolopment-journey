number1=int(input("Enter a number1"))
number2=int(input("Enter a number2"))
number3=int(input("Enter a number3"))

if number1>number2 and number2>number3:
    print("Number on is greater than")

elif number2>number1 and number2>number3:
    print("Number 2 is greater")

elif number3>number1 and number3>number2:
    print("Number3 greater")

else:
    print("invalid")            