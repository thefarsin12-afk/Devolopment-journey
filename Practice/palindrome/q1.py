"""
1. Check whether a number is a Palindrome.
Example:
Input: 121
Output: Palindrome
Input: 123
Output: Not Palindrome
"""

def palindrome_number(number):

    original_number = number

    reverse = 0

    while number != 0 :

        last_digit = number % 10

        reverse = reverse * 10 + last_digit

        number = number // 10

    if original_number == reverse:
        print(f"Palindrome Number,{reverse}")

    else:
        print("Not Palindrome Number")        

palindrome_number(1331)        