#comperhension

"""arr = [1,2,3,4,5,6,7]
square = [num **2 for num in arr]
print(square)"""

arr = [1,2,3,4,5,6,7]

add_num = [num + 5 for num in arr]

print(add_num)

evens = [num for num in arr if num % 2 == 0]
print(evens)

odd = [num for num in arr if num % 2 !=0]
print(odd)

number_greater = [num for num in arr if num > 5]
print(number_greater)
