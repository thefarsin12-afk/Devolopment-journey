"""
Write a Python program that takes an integer from the user and counts
how many digits are even and how many digits are odd.
"""

def even_odd(number):

    even_count = 0

    odd_count = 0

    while number > 0:

        last_digit = number % 10

        if last_digit % 2 == 0:
          
          even_count += 1

        else:

           odd_count += 1

        number = number // 10

    print("Even Digit = ",even_count)  

    print("Odd Digit =",odd_count)
           

even_odd(583246)           