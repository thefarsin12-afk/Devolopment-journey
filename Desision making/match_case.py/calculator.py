#set a calculator

number1 = int(input("Enter a number1...."))

number2 = int(input("Enter a number2...."))

option =(input("Enter a option +,-<*,/"))

match option:
    case "+":
        print(number1+number2)

    case "-":
        print(number1-number2)

    case "*":
        print(number1*number2)

    case "/":
        print(number1/number2)

    case _:
        print("Inavalid Enter")            

               
    