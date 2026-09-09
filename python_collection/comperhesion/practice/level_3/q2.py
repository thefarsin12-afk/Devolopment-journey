"""
2.  Convert negative numbers to 0 Input:[-5,10,-3,20,15]
    Output:[0,10,0,20,15]
"""
numbers = [-5,10,-3,20,15]

result = [0 if num < 0 else num  for num in numbers]
print(result)