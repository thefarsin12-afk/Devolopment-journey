num1 = int(input("Enter a number..."))

num2 = int(input("Enter a number..."))

option = input("Enter option min or max")

match option:

    case "min":

        if num1<num2:
            print("Min",num1)

        else:
            print("Min",num2)    

    case "max":
        if num1>num2:
            print("Max",num1)

        else:
            print("Max",num2)    

    case _:
        print("Invalid")        