"""
Right triangle

          *
         **
        ***  
       ****  
      *****
      5 r and 5 c  
"""
def space_star():

    for r in range(1,6):

        for s in range(5,r,-1):
            
            print(" ",end=" ")

        for c in range(1,r+1):

            print("*",end=" ")

        print()

space_star()                