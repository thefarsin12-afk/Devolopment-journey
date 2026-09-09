num1 = int(input("Enter a number...."))

num2 = int(input("Enter a number...."))

operations = input("Select operations + - *  / ")

result = 0
try:
    

    if operations == "+":

        result = num1 + num2

    elif operations == "-":

        result = num1 - num2

    elif operations == "*":

        result = num1 / num2            

    elif operations == "/":

        result = num1 * num2 

    else:

        print("Invalid attempt")

             

except Exception as e:

      print(e)

else:print(result)      

finally:
   
   print("db commit")

