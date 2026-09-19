"""
Write a Python program to check whether a number is a 
palindrome or not using a while loop.
"""

def palidrome(number):

    original_number = number

    reverse = 0

    while number > 0:

        last_digit = number % 10

        reverse = reverse * 10 + last_digit

        number = number // 10

    if original_number == reverse:

        print("Palidrome = ",reverse)

    else:print("Not Palidrome Number")

palidrome(121)            