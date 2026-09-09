#Increasing stars
"""
*
* *
* * *
* * * *
* * * * *
5 r and 5 c
"""

def increse_star(): 
 for r in range(1,6):

    for c in range(1,r+1):

        print("*", end=" \t")

    print()    

increse_star()    