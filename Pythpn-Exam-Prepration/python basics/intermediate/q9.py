"""
Write a Python program to check whether a number is a 
Strong Number or not using a while loop.
"""

def strong_number(number):

    original_number = number

    total = 0

    while number != 0:

        digit = number % 10

        factorial = 1

        for i in range(1,digit + 1):

         factorial = factorial * i

        total = total + factorial

        number = number // 10

    if original_number == total:
        print("Strong Number",total)

    else:print("Not Strong Number")

strong_number(145)            