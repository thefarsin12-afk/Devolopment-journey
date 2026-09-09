"""
     *
    * *
   *   *
  *     *
 *       *
* * * * * *
6 row and 6 colum
"""

for r in range(7,0,-1):

    for s in range(1,r):

        print(" ",end=" ")

    for c in range(1,(7-r)+1):

        print("*  ",end=" ")

    print()

