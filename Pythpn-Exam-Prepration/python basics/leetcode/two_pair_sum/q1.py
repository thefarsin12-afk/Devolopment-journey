arr = [1,2,3,5,6,3]

target = 8

for num in arr:

    difference = target - num

    if difference in arr:

        print(difference,num)
        break