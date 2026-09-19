"""
Input:  [1, 2, 4, 5]
Output: 3
"""

arr = [1,2,4,5]

max_arr =max(arr)

min_arr =min(arr)

total = 0

for i in range(min_arr,max_arr+1):

    total = total + i

sum_arr =sum(arr)

if total != sum_arr:
    print(total - sum_arr,"is missing")

else:
    print("no missing")    