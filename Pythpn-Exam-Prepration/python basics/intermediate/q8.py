"""
Write a Python program to check whether a number is an 
Armstrong number or not using a while loop.
"""

def armstrong_number(number):

    original_number = number

    total = 0

    digit_count = len(str(number))

    while number != 0:

        digit = number % 10

        total = total + digit ** digit_count

        number = number // 10

    if original_number == total:

        print("Armstrong Number",total)

    else:print("Not Armstrong Number") 

armstrong_number(153)           