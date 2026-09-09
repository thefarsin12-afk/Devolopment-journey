""" 
  1 2 3 4 5
  1 2 3 4
  1 2 3
  1 2 
  1
  row = 5
  colum = 5 to 1 inverted
"""

def inverted():

    for r in range(5,0,-1):

        for c in range(1,r+1,1):

            print(c,end="\t")
        
        print()

inverted()        

"""
for r in range(1,6):

    for c in range(1,r+1):

        print(c,end="\t")

    print()    
"""

