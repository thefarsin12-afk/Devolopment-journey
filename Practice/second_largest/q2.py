#1. Second Largest among 4 Numbers

def second_largest(num1,num2,num3,num4):

    if num1 >= num2 and num1 >= num3 and num1>= num4:
        if num2 >= num3 and num2 >= num4:
            print(f"Second largest number is {num2}")

        elif num3 >= num2 and num3 >= num4:
            print(f"Second largest number is {num3}")

        else:
            print(f"Seconfd largest number is {num4}")        

    elif num2 >= num1 and num2 >= num3 and num2 >= num4:

        if num1 >= num3 and num1 >= num4 :
            print(f"Second largest number {num1}")

        elif num3 >= num1 and num3 >= num4:
            print(f"Second largest number is {num3}")

        else:
            print(f"Second largest number is {num4}")  

    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        if num1 >= num2 and num1 >= num4:
            print(f"SEcond largest number is {num1}")

        elif num2 >= num1 and num2 >= num4 :
            print(f"Second largets number is {num2}")  

        else:
            print(f"Second largest number is {num4}")

    else:
         if num1 >= num2 and num1 >= num3:
            print(f"Second largest number is {num1}")

         elif num2 >= num1 and num2 >= num3:
            print(f"Second largest number {num2}")

         else:
            print(f"Second largest number is {num3}") 

second_largest(20,45,40,50)                                           