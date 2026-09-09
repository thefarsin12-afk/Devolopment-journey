array = [10,1,15,16,11,10,12,11]

array_set = set(array)

num_count = {}

for num in array_set:

    num_count[num] = array.count(num)

print(num_count)    