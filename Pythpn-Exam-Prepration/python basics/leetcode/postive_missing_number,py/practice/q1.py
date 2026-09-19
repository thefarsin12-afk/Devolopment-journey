"""
Find the missing positive integer.
Input:  [1, 2, 4, 5]
Output: 3
"""

arr = [1,2,3,5]
    #  0 1 2 3

total = 0    

min_number = min(arr)

max_number = max(arr)

for i in range(min_number,max_number+1):

    total = total + i

arr_sum = sum(arr)

if total != arr_sum:
    print(total - arr_sum,"is missing")

else:print("no missing")        

    

