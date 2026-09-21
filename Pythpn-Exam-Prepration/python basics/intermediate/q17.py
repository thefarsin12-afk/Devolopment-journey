"""
Q8

numbers = [3, 2, 4]
target = 6

Find the indexes of the two numbers whose sum equals the target.

Expected:
[1, 2]
"""

arr = [3, 2, 4]

arr.sort()

target = 6

left = 0

right = len(arr)-1

while left < right:

    current_sum = arr[left]+arr[right]

    if current_sum == target:
        print(left,right)
        break

    elif current_sum > target:
        right = right -1

    elif current_sum < target:
        left = left + 1

else:print(-1)        

        