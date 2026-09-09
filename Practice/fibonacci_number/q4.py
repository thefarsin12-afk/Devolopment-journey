def fibonacci_number(number):

    f = 0

    s = 1

    for i in range (1,number):

     next = f + s

     f = s

     s = next

    print(f)

fibonacci_number(10)            