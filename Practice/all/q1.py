"""
2. Find the Smallest Digit in a Number.
Example:
Input: 58392
Output: 2
"""

def smallest_digit_nummber(number):

    smallest = 9

    while number != 0 :

        last_digit = number % 10

        if last_digit < smallest:
            smallest = last_digit

        number //= 10    

    print(smallest)

smallest_digit_nummber(1234)        
