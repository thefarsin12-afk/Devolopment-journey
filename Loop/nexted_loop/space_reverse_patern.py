"""
      *
     **
    ***
   ****
  *****
  r=5,s and=5
"""

def reverse_space_star():
 for r in range(5,0,-1): #1,2,3,4,5

    for s in range(1,r):#5,1,-1

        print(" ",end=" ") # space and end

    for c in range(1,(7-r)+1): #1,1+1

        print("*", end=" ") #space and end    

    print() #next line

reverse_space_star()    