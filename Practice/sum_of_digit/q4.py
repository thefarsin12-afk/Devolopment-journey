"""
4. Find the Sum of First and Last Digit
Example:
Input: 58392
Output: 7
Explanation:
First digit = 5
Last digit = 2
5 + 2 = 7
"""

number = int(input("Enter a number..."))

sum = 0

first_digit = 0

last_digit = 0

while number != 0:

    digit = number % 10

    