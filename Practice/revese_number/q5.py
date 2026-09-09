"""
Find the Largest Digit in a Number

Example:

Input: 58392
Output: 9
"""

number = 58392

largest = 0

while number != 0:

    last_digit = number % 10
 
    if last_digit > largest:
      largest = last_digit

    number = number // 10    

print(largest)    