
def largest_even_number():
 number = int(input("Enter a number"))

 while number !=0:

    last_digit = number % 10

    if last_digit % 2 ==0:

        print(number)
        break
    
    else:
        number = number //10

largest_even_number()