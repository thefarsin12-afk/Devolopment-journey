# least positive missing number

arr = [1,2,3,5]

#step 1: find min ,and max in arr store to variable

min_number = min(arr)

max_number = max(arr)

#step 2: set total as 0

total = 0

#step 3:repeated chk each number from  min_number to max_number

for i in range(min_number,max_number+1):

    #step 4:then find min_number,max_number total and store total
    total = total +i

#step 5:find sum of arr store to variable
arr_sum =sum(arr)

#step 6:check to tatal and arr_sum defrent
if total != arr_sum:

    #step 7: then print total and arr_sum defrence
    print(total-arr_sum ,"is missing")

else:print("no missing")    

