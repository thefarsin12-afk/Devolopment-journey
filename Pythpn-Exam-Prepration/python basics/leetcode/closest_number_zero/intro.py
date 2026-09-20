arr = [-2,3,1,2]

#step 1:set closest as arr index[0]
closest = arr[0]

#step 2:repeated check each number in arr
for num in arr:

    #step 3: check abs(num)<abs(closest)
    if abs(num) < abs(closest):

        #step 4: then num  store to closest
        closest = num

#print(closest)
print(closest)