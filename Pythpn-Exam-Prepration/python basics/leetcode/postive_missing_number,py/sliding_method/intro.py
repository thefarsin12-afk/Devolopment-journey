arr = [1,3,2,5,4,7]
#      0 1 2 3 4 5
#      l r

#step1: sort to arr
arr.sort()

#step2: set left to 0 beacues left starting 0 index
left = 0

#step3 :repeated while to left < length of arr and -1 (becuese len(arr) = 6-1 = 5, left<5 =4,left work to 4 ) 
while left < len(arr) -1:

    #step 4: then set right left to right
    right = left + 1

    #step 5: find defference to left to right index
    defference = arr[right] - arr[left]

    #step 6: then check to defference not equal to 1
    if defference != 1:

        #step 7: then print arr[left] index +1 is missing then exit
        print( arr[left]+1,"is missing" )
        break

    #another wise (defrent equal to 1) set left = left +1
    else:left = left +1    