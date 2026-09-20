"""
Q12 — Negative Closest
nums = [-10, -5, -3, -8]

Output:
-3
"""

arr = [-10, -5, -3, -8]

closest = arr[0]

for num in arr:

    if abs(num) < abs(closest):

        closest = num

print(closest)        