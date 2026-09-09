"""
Find the Sum of the Digits

Example:

Input: 1234
Output: 10

(1 + 2 + 3 + 4 = 10)
"""
number = 1234

sum = 0

while number != 0:

    last_digit = number % 10

    sum = sum + last_digit

    number = number // 10

print(sum)    