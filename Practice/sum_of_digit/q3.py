"""
3. Find the Sum of Odd Digits in a Number
Example:
Input: 58392
Output: 17
Explanation:
5 + 3 + 9 = 17
"""

number = int(input("Enter a number..."))

sum  = 0

while number != 0:

    digit = number % 10

    if digit % 2 != 0:

        sum = sum + digit

    number = number // 10

print(sum)        