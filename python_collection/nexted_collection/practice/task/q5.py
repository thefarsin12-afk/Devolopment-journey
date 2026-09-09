"""
5.Find the smallest element in a list.
"""

numbers = [10,11,12,13,14,15]

#method1
print(min(numbers))

#method2
smallest_number = numbers[0]

for num in numbers:

    if num < smallest_number:

        smallest_number = num

print(smallest_number)        