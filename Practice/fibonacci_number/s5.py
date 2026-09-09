#Find the sum of all odd Fibonacci numbers up to n.

def fibonacci_number(number):

    first = 0

    second = 1

    sum = 0

    while first <= number:

        if first % 2 != 0:

            sum += first

        next_number = first + second

        first = second

        second = next_number

    print(sum)

fibonacci_number(20)            