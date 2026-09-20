"""
nums = [2, 7, 11, 15]
target = 9

output = [0, 1](index)
"""

arr = [2,7,11,15]

target = 9

left = 0

right = len(arr)-1

while left < right:

    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print(left,right)
        break

    elif current_sum > target:

        right = right -1

    elif current_sum < target:

        left = left + 1

else:print(-1)       