def fibonacci_number(n):

    f = 0

    s = 1

    for i in range (n):

     print(f)

     

     next = f + s

     f = s

     s = next    

fibonacci_number(5)    