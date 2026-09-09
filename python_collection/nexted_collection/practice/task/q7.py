"""
7.Calculate the average of the numbers in a list.
"""

number = [10,11,12,13,14,15]

#method1
print(sum(number)/len(number))

#method2
total = 0
for num in number:

    total += num

    average = total / len(number)

print(average)    