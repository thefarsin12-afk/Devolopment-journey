"""
4. Count the Even Digits in a Number.
Example:
Input: 58392
Output: 2
Even digits are:
8, 2
"""
def count_even(number):

 count = 0

 while number != 0:

    last_digit = number % 10

    if last_digit % 2 == 0:
        
        count = count + 1

    number = number // 10    

 print(count)

count_even(58392) 