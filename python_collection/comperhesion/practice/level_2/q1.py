"""
1. Extract even numbers Input: numbers=[3,8,15,22,10,5] Expected
Output: [8,22,10]
"""

number = [3,8,15,22,10,5]

even_number = [num for num in number if num % 2 == 0]

print(even_number)