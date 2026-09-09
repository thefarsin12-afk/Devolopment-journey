#Find the minimum of 3 numbers.

def minimum_number(num1,num2,num3):
    
    if num1 <= num2 and num1 <= num3:
        print(f"Minimum number is {num1}")

    elif num2 <= num1 and num2 <= num3:
        print(f"Minimum number is {num2}") 

    else:
        print(f"Minimum nuber is {num3}")       

minimum_number(12,13,43)        