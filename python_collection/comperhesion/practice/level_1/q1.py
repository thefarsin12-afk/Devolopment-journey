# 1. Create a list of squares Input: numbers = [1,2,3,4,5] Output:
#[1,4,9,16,25]

number = [1,2,3,4,5]
"""
square =[]
for num in number:
 
 square_add =  num * num

 square.append(square_add)

print(square)"""

#comperhension

square_add = [num * num for num in number]

print(square_add)
