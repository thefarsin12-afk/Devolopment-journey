"""
5.  Extract numbers divisible by 5 Input: numbers=[12,15,20,33,40,51]
    Expected Output: [15,20,40]
"""
numbers = [12,15,20,33,40,51]

result = [num for num in numbers if num % 5 == 0]

print(result)

for num in numbers:

    if num % 5 == 0:

        result.append(num)

