"""
10.Print all numbers greater than 50 from a list.
"""

number = [10,20,30,40,50,60,70]

#comperhension method
result = [num for num in number if num > 50]
print(result)

#method
for num in number:

    if num > 50:

        result.append(num)

