"""
5. Find the Digital Root of a Number
(Keep adding digits until one digit remains)
Example:
Input: 9875
Process:
9 + 8 + 7 + 5 = 29
2 + 9 = 11
1 + 1 = 2
Output:
2
"""
number = 9875

while number >= 10:

    sum = 0

    while number != 0:

        last_digit = number % 10

        sum = sum + last_digit

        number = number // 10

    number = sum

print (number)