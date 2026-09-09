"""
4.Find the largest element in a list.
"""

number = [10,11,12,13,14,15]

#method1
print(max(number))

#method2
largest = number[0]

for num in number:

    if num > largest:

        largest = num
           