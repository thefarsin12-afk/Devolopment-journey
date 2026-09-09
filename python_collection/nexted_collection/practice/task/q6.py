"""
6.Calculate the sum of all elements in a list.
"""

numbers = [10,11,12,13,14,15]

#all sum method
print(sum(numbers))

#indvdual sum method
result = []

for num in numbers:

    result.append(num + num)

print(result)    
