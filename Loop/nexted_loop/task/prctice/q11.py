def hollo_triankile(row):

    

    for r in range(1,row + 1):

        for c in range (1,r + 1):

              if c == 1 or c == r or r == row:
                  print("*" , end=" ")

              else:
                   print(" " , end=" ")       
        print()   

hollo_triankile(5)                 