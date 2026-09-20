arr = [1000,100,10,20,300,2000]

reverse = []

for i in range(0,len(arr)):

    popped_arr = arr.pop()

    reverse.append(popped_arr)

print(reverse)    