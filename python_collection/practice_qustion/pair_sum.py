#method1
#pair number sum and target
arr = [2,3,4,5,8]

target = 8

for n1 in arr:

    for n2 in arr:

        total = n1 + n2

        if target == total and n1 != n2:
            print(n1,n2)
            break

#method 2
arra = [1,4,6,8,9]

target = 9

for n in arra:

    diference = target - n

    if diference in arra and diference != n :
        print(diference,n)
        break