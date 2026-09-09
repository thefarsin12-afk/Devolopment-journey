"""
Count the odd Fibonacci numbers up to n.
"""

n = int(input("Enter a number..."))

f = 0

s = 1

c = 0

while f <= n:

    if f % 2 != 0:
        
     c += 1

    next_number = f + s

    f = s

    s = next_number
 
print(c)    