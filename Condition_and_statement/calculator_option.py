number1 = int(input("Enter a number..."))

number2 = int(input("Enter a number..."))

option = (input("Select option +,-,*,/")) 

if option == "+":
    print(number1+number2)

elif option == "-":
    print(number1-number2)

elif option == "*":
    print(number1*number2)

elif option == "/":
    print(number1/number2)

else:
    print("Invalid option")    
