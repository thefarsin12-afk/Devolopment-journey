"""
5. Reverse List

Q9

Reverse the list without using reverse() or [::-1]:

numbers = [1, 2, 3, 4, 5]

Expected:
[5, 4, 3, 2, 1]
"""

arr = [1, 2, 3, 4, 5]

reversed = []

for num in range(0,len(arr)):

    popped_lst = arr.pop()
    reversed.append(popped_lst)

print(reversed)    