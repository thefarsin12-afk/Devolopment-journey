arr = [2,-2,1,-1]

closest = arr[0]

for num in arr:

    if abs(num) < abs(closest):

        closest = num

if closest < 0 and abs(closest):
    print(abs(closest))

else:
    print(closest)        