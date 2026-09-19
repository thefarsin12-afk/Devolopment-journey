# given a arr .want to target number pair
arr = [2,3,4,5,6]

target = 9

#step1: repeated check each number in arr
for num in arr:

    #step2: check differnce target and num
    difference = target - num

    #step3: then check to difference included arr
    if difference in arr:

        #step4: print difference and num (pair)
        print(f"Pair = {num},{difference}")
        break

