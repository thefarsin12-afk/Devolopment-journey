"""
nums = [1, 5, 8, 10]
target = 20

out put = -1,-1
"""

arr = [1,5,8,10]

target = 20

left = 0

right = len(arr)-1

while left < right:

    current_arr = arr[left] + arr[right]

    if current_arr == target:
        print(arr[left],arr[right])
        break

    elif current_arr > target:

        right = right - 1

    elif current_arr < target:

        left = left + 1

else:print(-1,-1)            