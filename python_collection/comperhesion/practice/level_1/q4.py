"""
4.  Multiply every number by 10 Input: numbers=[2,5,8,10] Output:
    [20,50,80,100]
"""

number = [2,3,8,10]

output = [num * 10 for num in number]
print(output)

for num in number:

    multiplication = num * 10

    output.append(multiplication)

