"""
nums = [1, 5, 8, 10]
target = 20

Output: [-1, -1]
"""

arr = [1, 5, 8, 10]

target = 20

left = 0

right = len(arr)-1

while left < right:

    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print(arr[left],arr[right])
        break

    elif current_sum > target:
        right = right -1

    elif current_sum < target:
        left = left +1

else:
    print(-1,-1)    