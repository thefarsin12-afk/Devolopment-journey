arr = [2,1,-4,-1]

closest = arr[0]

for num in arr:

    if abs(num) < abs(closest):
        closest = num

print(closest)        