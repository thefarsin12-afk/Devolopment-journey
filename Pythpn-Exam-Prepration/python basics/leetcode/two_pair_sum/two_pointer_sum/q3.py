"""
nums = [3, 2, 4]
target = 6

Output: [1, 2]
"""

arr = [3,2,4]

arr.sort()

target = 6

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