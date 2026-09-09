"""
2. Find the Sum of Even Digits in a Number
Example:
Input: 58392
Output: 10
Explanation:
8 + 2 = 10
"""

number = int(input("Enter a number..."))

sum = 0
 
while number != 0:

 digit = number % 10

 if digit % 2 == 0:
   
   sum = sum + digit

 number = number // 10

print(sum)   
