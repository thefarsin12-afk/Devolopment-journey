"""
nums = [2, 7, 11, 15]
target = 9

Output: [0, 1] index value
"""

arr = [2,7,11,15]

target = 9

arr.sort()

left = 0

right = len(arr)-1

while left < right:

    cuurent_arr = arr[left] + arr[right]

    if cuurent_arr == target:

        print(left,right)
        break

    elif cuurent_arr > target:

        right = right - 1

    elif cuurent_arr < target:

        left = left + 1     