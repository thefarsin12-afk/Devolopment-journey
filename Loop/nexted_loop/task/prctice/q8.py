#Inverted right triangle
"""
5 r, 5 c and space
"""

def reverse_space_number():
 for r in range(5,0,-1):

    for s in range(5,r,-1):

        print(" ", end=" ")

    for r in range(1,r+1):
        
        print("*", end = " ")

    print()

reverse_space_number()            
