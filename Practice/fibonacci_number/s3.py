#Count the even Fibonacci numbers up to n.

def fibonacc_number(number):

    first = 0

    second = 1

    count = 0

    while first <= number:

        if first % 2 ==0:
            
            count += 1

        next_number = first + second

        first = second

        second = next_number

    print(count)

fibonacc_number(8)        
fibonacc_number(20)        