arr = [1,2,3,4,6]

min_number = min(arr)

max_number = max(arr)

total = 0

for i in range(min_number,max_number +1):

    total = total + i 

arr_sum = sum(arr)

if total != arr_sum:

    print(total - arr_sum,"is missing")

else:
    print("no missing")    