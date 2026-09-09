def hollo_pyramid():#refered

    row = 5

    for r in range (1,row +1):
     
      for s in range(row - r):
         
         print(" " ,end="")

      for c in range(1,2*r):

       if c ==1 or c == (2*r - 1) or r == row:

          print("*", end="")

       else:

          print(" ",end = "")

      print()      

hollo_pyramid()                 