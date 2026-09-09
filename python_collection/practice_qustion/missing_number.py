#method 1
arr = [1,2,3,4,6]

max_num = max(arr)

total = 0

for num in range(1,max_num +1):

    total = total + num

    curent_arr = sum(arr)

    diference = total - curent_arr

print(diference)    

#method 2
arra = [1,2,3,4,5,7]
#index  0 1 2 3 4 5
#       p c

arra.sort

for p in range(0,len(arra)-1):

    c = p + 1

    diference1 = arra [c] - arra[p]

if diference1 != 1:
    print("missing number is" ,arra[p]+1)