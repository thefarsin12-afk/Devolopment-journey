"""
1. Find the Sum of Digits of a Number
Example:
Input: 12345
Output: 15
Explanation:
1 + 2 + 3 + 4 + 5 = 15
"""

number = int(input("Enter a number"))

sum = 0

while number != 0:

    last_digit = number % 10

    sum = sum + last_digit

    number = number // 10

print(sum)    