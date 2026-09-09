"""
q2) write a program to print duplicate numbers
    arr=[10,1,15,16,11,10,12,11]
    o/p => [10,11]
"""
"""araay = [10,1,15,16,11,10,12,11]

duplicate_arr = []

for num in araay:

    if araay .count(num)>1 and num not in duplicate_arr:

        duplicate_arr.append(num)

print(duplicate_arr)       """

array = [10,11,12,13,10,11,10,1]

duplicate_array = set()

for i in range (0,len(array)):

    for j in range (0,len(array)):

        if array[i] == array[j] and i != j:

            duplicate_array.add(array[i])

print(duplicate_array)            