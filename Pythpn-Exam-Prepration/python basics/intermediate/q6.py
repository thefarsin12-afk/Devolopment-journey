"""
Write a Python program to find the factorial of a 
given number using a for loop.
"""

def factorial_number(number):

    factorial = 1

    for i in range(1,number + 1):

        factorial = factorial * i

    print(factorial)

factorial_number(5)            