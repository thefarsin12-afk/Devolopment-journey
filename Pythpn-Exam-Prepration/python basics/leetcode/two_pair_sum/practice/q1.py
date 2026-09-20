"""
nums = [2, 7, 11, 15]
target = 9

Output: [0, 1]
"""

arr = [2,7,11,15]

target = 9

for num in arr:

    difference = target - num

    if difference in arr:

     print("is missing",difference,num)
     break