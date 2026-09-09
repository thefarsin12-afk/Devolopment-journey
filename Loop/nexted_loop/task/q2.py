"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
five rows
and five to 1 colum invert
"""

def inverted (number):

    for r in range(5,0,-1):

        for c in range(1,r+1):

            print(r,end="\t")

        print() 

inverted(print)            