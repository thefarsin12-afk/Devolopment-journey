#Check whether a number is Fibonacci.

def fibonacci_number(number):

    first = 0

    second = 1

    while first <= number:

        if number < 0:

            print("Note fibonicc number")

        if first == number:

            print("Fibonacci number")
            break

        next = first + second

        first = second

        second = next

    else:print("Note fibonacci number")

fibonacci_number(-1)        