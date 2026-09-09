"""
* * * * * * 6 row 0 space 6 colum 
 * * * * *  6 row 1 space 5 colum
  * * * *   6 row 2 space 4 colum
   * * *    6 row 3 space 3 colum
    * *     6 row 4 space 2 colum
     *      6 row 5 space 1 colum
"""
def reverse_pyramid():

 for r in range(6,0,-1):
   
   for s in range(1,(6-r)+1):
     
      print(" ",end=" ")

   for c in range(1,r+1):

      print("*  ", end=" ")

   print()

reverse_pyramid()         