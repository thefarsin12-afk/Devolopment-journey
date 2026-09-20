arr = [1,10,2,200,3,300]

#step 1: create an empty list
reverse = []

#step 2: repeated each length of num from arr,using to for loop
for num in range(0,len(arr)):

    #step 3:create variable and using to pop()
    popped_arr = arr.pop()

    #step 4:then store to reverse list
    reverse.append(popped_arr)

#print popped_arr 
print(reverse)   