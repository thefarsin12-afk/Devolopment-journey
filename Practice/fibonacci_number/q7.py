#Print only the even Fibonacci numbers up to n.
def fibonacci_number(number):

    first = 0

    second = 1

    while first <= number:

     if first % 2 ==0:
      print(first)
    

     next_number = first + second

     first = second

     second = next_number

fibonacci_number(8)            