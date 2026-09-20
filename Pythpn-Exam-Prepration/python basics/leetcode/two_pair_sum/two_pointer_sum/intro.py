arr = [1,3,2,5,4,7,6]

target = 9

#step 1: sort arr
arr.sort()

#step 2: left as 0 [seting index]
left = 0

#step 3:right as len(arr)-1 (exact index given)
right = len(arr)-1

#repeated while left < right beacuse two no swap and not equal
while left < right:

    #step 5: find current sum arr
    
    current_sum = arr[left] + arr[right]

    #step 6:check target and current sum equal
    if current_sum == target:

        #step 7:then print arr[left],arr[right] pait then exit
        print(arr[left],arr[right])
        break

    #check current_sum greter than target then right -1
    elif current_sum > target:

        right = right -1

    #check current_sum less than target the left +1
    elif current_sum < target:

        left = left +1    