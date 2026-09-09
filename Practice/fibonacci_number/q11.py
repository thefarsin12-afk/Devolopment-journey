#Find the largest Fibonacci number less than or equal to n.

def fibanacci_number(number):

    first = 0

    second = 1

    largest = 0

    while first <= number:

        largest = first

        next_number = first + second

        first = second

        second = next_number

    print(largest)    

fibanacci_number(9)            