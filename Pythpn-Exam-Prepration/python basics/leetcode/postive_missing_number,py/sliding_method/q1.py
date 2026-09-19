arr = [1,4,2,3,6]

arr.sort()

l = 0

while l < len(arr)-1:

    r = l+1

    defference = arr[r] - arr[l]

    if defference != 1:
        print(arr[l]+1,"is missing")
        break

    else:
        l = l+1     