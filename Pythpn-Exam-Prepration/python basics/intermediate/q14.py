"""
3. Least Positive Missing Integer

numbers = [3, 4, -1, 1]

Find the smallest positive missing integer.

Expected:
2
"""

numbers = [3, 4, -1, 1]

number = 1

while number in numbers:

    number = number +1

print(number)    