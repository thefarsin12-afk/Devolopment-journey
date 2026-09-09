"""
     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *

row = 6,space,5 and decrese,c=1,6

"""

def pyramid():

 for r in range(6,0,-1):

    for s in range(1,r):

        print(" ",end=(" "))

    for c in range(1,(7-r)+1):

        print("*  " , end=" ")

    print()    

pyramid()            