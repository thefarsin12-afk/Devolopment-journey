#Print the first 20 Fibonacci numbers using a while loop.
def fibonicc_number(number):

    first = 0

    second = 1

    count = 0

    while count <20:

        print(first)

        next_number = first + second

        first = second

        second = next_number

        count += 1

fibonicc_number(5)
        