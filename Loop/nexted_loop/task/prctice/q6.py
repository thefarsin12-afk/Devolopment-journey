#Decreasing stars
"""
* * * * *
* * * * 
* * * 
* * 
* 
5 r and 5 c
"""

def reverse_star():
 for r in range (5,0,-1):

    for c in range (1,r+1):

        print("*", end=" ")

    print()   

reverse_star()    