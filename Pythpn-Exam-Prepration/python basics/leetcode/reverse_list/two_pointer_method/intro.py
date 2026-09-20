arr = [1,3,200,40,500]

#step 1: set left as 0
left = 0 

#step 2: right as length of arr and -1(exact index value give -1)
right = len(arr)-1

#step 3:repeated while left lessthan right:
while left < right:

    #step 4:swaping
    (arr[left],arr[right]) = (arr[right],arr[left])

    #step 5:left = left +1
    left = left +1

    #right = right -1
    right = right -1

#print arr
print(arr)    