"""
1. Check if a Number is a Palindrome
Question:
Write a function that checks whether a given number is a palindrome.

Example:
Input: 121
Output: Palindrome

Input: 123
Output: Not Palindrome
"""
def palidrome(number):

    original_number = number

    reverse = 0

    while number != 0:

        last_digit = number % 10

        reverse = reverse * 10 + last_digit

        number = number // 10

    if original_number == reverse:
        print(f"Palidrome Number ,{reverse}")

    else:print("Not palidrome number")        

palidrome(123)        

