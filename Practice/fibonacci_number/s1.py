"""
Print Fibonacci numbers between a and b.

Example: a = 5, b = 30
Output: 5 8 13 21
"""

num1 = int(input("Enter number..."))

num2 = int(input("Enter number..."))

first = 0

second = 1

while first <= num2:
 
 if first >= num1:
  print(first)


 next_number = first +  second

 first = second

 second = next_number
    


      
