arr = [10,11,1,10,11,2,3]

unique_number = [num for num in arr if arr.count(num) ==1]
print(unique_number)

dublicate_number = {num for num in arr if arr.count(num) > 1}
print(dublicate_number)