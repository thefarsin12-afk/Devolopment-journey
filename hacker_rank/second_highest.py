#identfy secong highest number in arr

arr = [2,3,6,6,5]

highest = max(arr)

while highest in arr:

    arr.remove(highest)

print(max(arr))