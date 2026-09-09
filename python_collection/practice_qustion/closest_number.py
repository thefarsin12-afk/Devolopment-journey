arr = [ -3,-2,-1,3,4]

closest = arr [0]

for number in arr:

    if abs(number) < abs(closest):

        closest = number

print(closest)    