arr = [20,12,30,500]

reverse = []

for i in range(0,len(arr)):

    popped_element = arr.pop()

    reverse.append(popped_element)

print(reverse)    