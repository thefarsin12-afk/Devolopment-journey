"""
6. Closest Number to Zero
numbers = [-4, -2, 1, 4, 8]

Find the number closest to zero.

Expected:
1
"""

arr = [-4, -2, 1, 4, 8]

closest = arr[0]

for num in arr:

    if abs(num) < abs(closest):
        closest = num

if closest < 0 and abs(closest) in arr:

    print(abs(closest))

else:print(closest)    


