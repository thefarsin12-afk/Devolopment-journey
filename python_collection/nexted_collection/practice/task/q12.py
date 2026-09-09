"""
12.Find all prime numbers in a list.
"""

number = [2,5,7,9,13,15,18]

for num in range (2,len(number)):

    if number % num == 0:
        break

else:print(num)

