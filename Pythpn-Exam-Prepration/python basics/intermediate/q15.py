"""
Q6
numbers = [7, 8, 9, 11, 12]
Find the smallest positive missing integer.

Expected:
1
"""

arr =[7, 8, 9, 11, 12]

number = 1

while number in arr:

    number = number + 1

print(number)    