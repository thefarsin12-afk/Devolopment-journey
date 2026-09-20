"""
Q8 — Mixed Values
nums = [10, 20, 30, 40, 50, 60]

Output:

[60, 50, 40, 30, 20, 10]
"""

arr = [10, 20, 30, 40, 50, 60]

left = 0

right = len(arr)-1

while left < right:

    (arr[left],arr[right]) = (arr[right],arr[left])

    left = left + 1

    right = right -1

print(arr)    