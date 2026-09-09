"""
8.Find all even numbers in a list.
"""

number = [10,11,12,13,14,15]

#comperhension
result = [num for num in number if num % 2 == 0]
print(result)

#method
for num in number:

    if num % 2 == 0:

        result.append(num)
         