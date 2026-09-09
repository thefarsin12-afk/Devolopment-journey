"""
2.Create a list and Print elements is divisible by 3.
LIST=[1,4,6,9,12,25,24]
"""

numbers = [1,4,6,9,12,25,24]

result = []

for num in numbers:

    if num % 3 == 0:

        result.append(num)

print(result)        