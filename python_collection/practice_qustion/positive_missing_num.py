"""
q5) write a program to print least +ve missing number 
     arr=[1,2,4,5]
     o/p => 3
"""

array = [1,2,4,5]

postive_number = 1

while postive_number in array:

    postive_number += 1

print(postive_number)    

"""
 eg2:
    arr=[1,3,4,5]
     o/p => 2
"""

array = [1,3,4,5]

postive_num = 1

while postive_num in array:

    postive_num = postive_num + 1

print(postive_num)    