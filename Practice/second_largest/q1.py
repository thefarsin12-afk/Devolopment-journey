#Find the second largest among 3 numbers.

def second_largest(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            print(f"Second largest number is {num2}")

        else:
            print(f"Second largest number is {num3}") 


    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            print(f"Second largest number is {num1}") 

        else:
            print(f"Second Largest number is {num3}")   


    else:
        if num1 >= num2:
         print(f"Second largest number is {num1}")                   

        else:
            print(f"Second largest number is {num2}") 

second_largest(10,20,30)            
second_largest(35,40,30)            