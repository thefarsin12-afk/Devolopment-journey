"""
numbers = [-7, -2, 5, 9]

Find the number closest to zero.

Expected:
-2
"""

arr = [-7, -2, 5, 9]

closest = arr[0]

for num in arr:

    if abs(num) < abs(closest):
        closest = num


if closest <0 and abs(closest) in arr:
    print(abs(closest))

else:print(closest)             