#Count how many Fibonacci numbers are less than or equal to n.

def fibonicc_number(number):

    first = 0

    second = 1

    count = 0

    while first <= number:

        count += 1

        next = first + second

        first = second

        second = next

    print(count)
  
fibonicc_number(8)    