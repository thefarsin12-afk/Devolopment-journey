"""
11.Print all numbers less than 20 from a list.
"""

number = [5,10,15,20,25,30]

#comperhension
result = [num for num in number if num < 20]
print ( result)

#method
for num in number:

    if num < 20:
        result.append(num)

